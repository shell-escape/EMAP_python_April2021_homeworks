from unittest.mock import MagicMock

import homework_10.task_1
from homework_10.task_1 import (
    get_company_detailed_information,
    get_dollar_rate,
    get_index_result,
)


def test_get_dollar_rate(test_data_path, monkeypatch):
    """Testing 'get_dollar_rate' function."""
    test_filename = "XML_daily.asp"
    test_file_path = test_data_path.joinpath("homework_10", test_filename)

    mock = MagicMock()

    def get(arg):
        mock = MagicMock()
        with open(test_file_path, "rb") as fi:
            mock.content = fi.read()
        return mock

    mock.get = get

    monkeypatch.setattr("homework_10.task_1.requests", mock)

    dollar_rate = get_dollar_rate()

    assert dollar_rate == 30.9436


def test_get_company_detailed_information(test_data_path):
    """Testing 'get_company_detailed_information' function."""
    test_filename = "3M"
    tmp_dir = test_data_path.joinpath("homework_10")

    homework_10.task_1.tmp_dir = tmp_dir
    homework_10.task_1.dollar_rate = 2

    result = get_company_detailed_information(test_filename)

    assert result["name"] == "3M Co."
    assert result["code"] == "MMM"
    assert result["price"] == 405.6
    assert result["pe"] == 19.91
    assert result["potential_profit"] == 60.15


def test_get_index_result():
    """Tesing 'get_index_result' function."""
    companies_information = {
        "C1": {"name": "Company_1", "code": "1", "price": 100, "pe": 10},
        "C2": {"name": "Company_2", "code": "2", "price": 200, "pe": 20},
        "C3": {"name": "Company_3", "code": "3", "price": 300, "pe": 30},
    }

    homework_10.task_1.companies_information = companies_information

    price_result = get_index_result("price")
    assert price_result == [
        {"name": "Company_3", "code": "3", "price": 300},
        {"name": "Company_2", "code": "2", "price": 200},
        {"name": "Company_1", "code": "1", "price": 100},
    ]

    pe_result = get_index_result("pe")
    assert pe_result == [
        {"name": "Company_1", "code": "1", "pe": 10},
        {"name": "Company_2", "code": "2", "pe": 20},
        {"name": "Company_3", "code": "3", "pe": 30},
    ]
