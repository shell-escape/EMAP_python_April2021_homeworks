"""
Ваша задача спарсить информацию о компаниях, находящихся в индексе
S&P 500 с данного сайта:
https://markets.businessinsider.com/index/components/s&p_500

Для каждой компании собрать следующую информацию:
* Текущая стоимость в рублях (конвертацию производить по текущему курсу,
  взятому с сайта центробанка РФ (http://www.cbr.ru/development/sxml/))
* Код компании (справа от названия компании на странице компании)
* P/E компании (информация находится справа от графика
                на странице компании)
* Годовой рост/падение компании в процентах (основная таблица)
* Высчитать какую прибыль принесли бы акции компании (в процентах),
  если бы они были куплены на уровне 52 Week Low и проданы на уровне
  52 Week High (справа от графика на странице компании)

Сохранить итоговую информацию в 4 JSON файла:
1. Топ 10 компаний с самими дорогими акциями в рублях.
2. Топ 10 компаний с самым низким показателем P/E.
3. Топ 10 компаний, которые показали самый высокий
   рост за последний год.
4. Топ 10 комппаний, которые принесли бы наибольшую прибыль,
   если бы были куплены на самом минимуме и проданы на самом
   максимуме за последний год.

Пример формата:
[
{
    "code": "MMM",
    "name": "3M CO.",
    "price" | "P/E" | "growth" | "potential profit" : value,
},
...
]
For scrapping you cans use beautifulsoup4
For requesting aiohttp
"""

import asyncio
import json
import os
import shutil
import time
from concurrent.futures import ProcessPoolExecutor

import aiohttp
import requests
from bs4 import BeautifulSoup


def get_dollar_rate() -> float:
    """The current rate of US dollar in rubles from cbr.ru.

    Returns:
        USD to RUB rate.
    """
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "xml")
    dollar_value = soup.find(ID="R01235").Value
    return float(dollar_value.string.replace(",", "."))


async def save_companies_urls(url: str):
    """Add links and 1-year growh of s&p companies from page
    given by 'url' to global 'companies_information' dictionary.

    Args:
        url: the link to markets.businessinsider.com s&p page.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.read()
            soup = BeautifulSoup(text, "html.parser")
            for company_block in soup.find_all("tr")[1:]:
                company_line = company_block.find("a")
                company_name = company_line.get("title")
                company_href = company_line.get("href")
                company_link = "https://markets.businessinsider.com" + company_href
                company_growth = float(
                    company_block.find_all("span")[9].text.strip("%").replace(",", "")
                )
                companies_information[company_name] = {
                    "link": company_link,
                    "growth": company_growth,
                }


async def download_html(url: str, filename: str, session: aiohttp.ClientSession):
    """Download html from 'url' to file with 'filename' name.

    Args:
        url: link to download html.
        filename: file name to save html.
        session: session object.
    """
    async with session.get(url) as response:
        text = await response.read()
        soup = BeautifulSoup(text, "html.parser")
        with open(filename, "w") as fi:
            fi.write(str(soup))


async def download_companies_htmls():
    """Saves html pages of all s&p companies from
    markets.businessinsider.com."""

    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)
    os.makedirs(tmp_dir)

    pages = range(1, 11)
    urls = [
        f"https://markets.businessinsider.com/index/components/s&p_500?p={page}"
        for page in pages
    ]

    async with aiohttp.ClientSession() as session:
        main_pages_tasks = [
            asyncio.create_task(save_companies_urls(url)) for url in urls
        ]
        await asyncio.gather(*main_pages_tasks)

        company_pages_tasks = [
            asyncio.create_task(
                download_html(
                    companies_information[company]["link"],
                    f"{tmp_dir}/{company}.html",
                    session,
                )
            )
            for company in companies_information
        ]
        await asyncio.gather(*company_pages_tasks)


def get_company_detailed_information(company: str) -> dict:
    """Collect informaton from s&p company page:
    name, code, price, P/E ratio and potential profit.
    If the information about P/E ratio is absent, set it to inf.
    If the information about potential profit is absent, set it to -inf.

    Args:
        company: company file name.

    Returns:
        dictionary with corresponding information.
    """

    with open(f"{tmp_dir}/{company}.html") as fi:
        soup = BeautifulSoup(fi.read(), "html.parser")

    company_dict = {}

    name_chunk = soup.find("span", class_="price-section__label")
    company_dict["name"] = name_chunk.text.strip()

    code_chunk = soup.find("span", class_="price-section__category")
    company_dict["code"] = code_chunk.find("span").text.lstrip(", ")

    price_chunk = soup.find("span", class_="price-section__current-value")
    company_dict["price"] = round(
        float(price_chunk.text.replace(",", "")) * dollar_rate, 2
    )

    try:
        pe_chunk = soup.find(
            text="P/E Ratio", class_="snapshot__header"
        ).previous_sibling
        company_dict["pe"] = float(pe_chunk.strip().replace(",", ""))
    except AttributeError:
        company_dict["pe"] = float("inf")

    try:
        low_profit_chunk = soup.find(
            text="52 Week Low", class_="snapshot__header"
        ).previous_sibling
        low_profit = float(low_profit_chunk.strip().replace(",", ""))
        high_profit_chunk = soup.find(
            text="52 Week High", class_="snapshot__header"
        ).previous_sibling
        high_profit = float(high_profit_chunk.strip().replace(",", ""))
        company_dict["potential_profit"] = round(high_profit - low_profit, 2)
    except AttributeError:
        company_dict["potential_profit"] = float("-inf")

    return company_dict


def get_companies_detailed_information():
    """Apply 'get_company_detailed_information' function to all
    companies using multiprocessing."""
    with ProcessPoolExecutor() as pool:
        result = pool.map(get_company_detailed_information, companies_information)
        for company, company_dict in zip(companies_information, result):
            companies_information[company] |= company_dict


def get_index_result(index: str):
    """Select top 10 companies in 'index' indicator.

    Args:
        index: company indicator.

    Returns:
        dictionary with top 10 companies and corresponding information.
    """

    companies_result = []

    top_companies = sorted(
        companies_information,
        key=lambda x: companies_information[x][index],
        reverse=(index != "pe"),
    )[:10]

    for company in top_companies:
        companies_result.append(
            {
                "code": companies_information[company]["code"],
                "name": companies_information[company]["name"],
                index: companies_information[company][index],
            }
        )

    return companies_result


if __name__ == "__main__":

    companies_information = {}
    tmp_dir = "./_companies"

    t = time.time()
    asyncio.run(download_companies_htmls())

    print("downloading:", time.time() - t)  # noqa

    dollar_rate = get_dollar_rate()

    t = time.time()

    get_companies_detailed_information()

    print("parsing:", time.time() - t)  # noqa

    shutil.rmtree(tmp_dir)

    for index in ("price", "pe", "growth", "potential_profit"):
        with open(f"{index}.json", "w") as fi:
            json.dump(get_index_result(index), fi, indent=4)
