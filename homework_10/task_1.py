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
from concurrent.futures import ProcessPoolExecutor
from typing import Generator, List, Tuple

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


class CompaniesStorage:
    """Class to store information about S&P 500 companies.

    Args:
        main_url: url to markets.businessinsider.com S&P 500 page.
        pages_number: the number of pages with companies.

    Attributes:
        main_url: url to markets.businessinsider.com S&P 500 page.
        pages_number: the number of pages with companies.
        main_pages: main pages htmls.
        companies_pages: companies pages htmls.
        companies: information about companies.
    """

    def __init__(self, main_url: str, pages_number: int):
        self.main_url = main_url
        self.pages_number = pages_number
        self.main_pages = []
        self.companies_pages = []
        self.companies = {}

    def get_main_pages_urls(self) -> Generator[str, None, None]:
        """Generates urls of main pages.

        Yields:
            main pages urls.
        """
        return (f"{self.main_url}p={page}" for page in range(1, self.pages_number + 1))

    async def _save_html(
        self, url: str, storage: List, session: aiohttp.ClientSession, name=None
    ):
        """Appends HTML from 'url' to 'storage'. If 'name' is not None,
        appends it along with HTML.

        Args:
            url: url to html to save.
            storage: list to save the html.
            session: ClientSession object.
            name: if not None, also is appended to storage.
        """
        async with session.get(url) as response:
            text = await response.read()
            what_to_save = (name, text) if name else text
            storage.append(what_to_save)

    async def download_main_pages(self):
        """Saves html pages of all s&p companies from
        markets.businessinsider.com."""
        async with aiohttp.ClientSession() as session:
            main_pages_tasks = [
                asyncio.create_task(self._save_html(url, self.main_pages, session))
                for url in self.get_main_pages_urls()
            ]
            await asyncio.gather(*main_pages_tasks)

    def parse_main_pages(self):
        """Parses main pages and adds link and growth of companies
        to self.companies."""
        for main_page in self.main_pages:
            soup = BeautifulSoup(main_page, "html.parser")
            for company_block in soup.find_all("tr")[1:]:
                company_line = company_block.find("a")
                company_name = company_line.get("title")
                company_href = company_line.get("href")
                company_link = "https://markets.businessinsider.com" + company_href
                company_growth = float(
                    company_block.find_all("span")[9].text.strip("%").replace(",", "")
                )
                self.companies[company_name] = {
                    "link": company_link,
                    "growth": company_growth,
                }

    async def download_companies_pages(self):
        """Saves html pages of all s&p companies from
        markets.businessinsider.com."""
        async with aiohttp.ClientSession() as session:
            company_pages_tasks = [
                asyncio.create_task(
                    self._save_html(
                        self.companies[company]["link"],
                        self.companies_pages,
                        session,
                        name=company,
                    )
                )
                for company in self.companies
            ]
            await asyncio.gather(*company_pages_tasks)

    @staticmethod
    def parse_company_page(text_and_name: Tuple[str]) -> dict:
        """Collect informaton from s&p company page:
        name, code, price, P/E ratio and potential profit.
        If the information about P/E ratio is absent, set it to inf.
        If the information about potential profit is absent,
        set it to -inf.

        Args:
            text_and_name: text of company page and company short name.

        Returns:
            dictionary with corresponding information.
        """

        short_name, text = text_and_name
        soup = BeautifulSoup(text, "html.parser")
        company_dict = {}

        name_chunk = soup.find("span", class_="price-section__label")
        company_name = name_chunk.text.strip()
        company_dict["name"] = company_name
        company_dict[company_name] = short_name

        code_chunk = soup.find("span", class_="price-section__category")
        company_dict["code"] = code_chunk.find("span").text.lstrip(", ")

        price_chunk = soup.find("span", class_="price-section__current-value")
        company_dict["price"] = round(
            float(price_chunk.text.replace(",", "")) * get_dollar_rate(), 2
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

    def parse_companies_pages(self):
        """Apply 'get_company_detailed_information' function to all
        companies using multiprocessing and adds its result
        to self.companies."""
        with ProcessPoolExecutor() as pool:
            result = pool.map(
                CompaniesStorage.parse_company_page,
                self.companies_pages,
            )
        for company_dict in result:
            full_name = company_dict["name"]
            short_name = company_dict[full_name]
            self.companies[short_name] |= company_dict

    def get_index_result(self, index: str):
        """Select top 10 companies in 'index' indicator.

        Args:
            index: company indicator.

        Returns:
            dictionary with top 10 companies
            and corresponding information.
        """

        companies_result = []

        top_companies = sorted(
            self.companies,
            key=lambda company: self.companies[company][index],
            reverse=(index != "pe"),
        )[:10]

        for company in top_companies:
            companies_result.append(
                {
                    "code": self.companies[company]["code"],
                    "name": self.companies[company]["name"],
                    index: self.companies[company][index],
                }
            )

        return companies_result

    def generate_jsons(self, indices: Tuple[str]):
        """Starts full process for top 10 jsons generation.

        Args:
            indices: indices to generate jsons.
        """
        asyncio.run(self.download_main_pages())
        self.parse_main_pages()
        asyncio.run(self.download_companies_pages())
        self.parse_companies_pages()

        for index in indices:
            with open(f"{index}.json", "w") as fi:
                json.dump(storage.get_index_result(index), fi, indent=4)


if __name__ == "__main__":
    main_url = "https://markets.businessinsider.com/index/components/s&p_500?"
    storage = CompaniesStorage(main_url, 10)
    indices = ("price", "pe", "growth", "potential_profit")
    storage.generate_jsons(indices)
