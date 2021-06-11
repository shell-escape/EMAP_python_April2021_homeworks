from unittest.mock import MagicMock

from homework_10.task_1 import CompaniesStorage, get_dollar_rate


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


def test_companies_parsing(test_data_path, monkeypatch):
    """Testing 'get_company_detailed_information' method."""

    test_filename = "3M.html"
    test_file_path = test_data_path.joinpath("homework_10", test_filename)

    with open(test_file_path) as fi:
        text = fi.read()
    text_and_name = ("3M", text)

    monkeypatch.setattr("homework_10.task_1.get_dollar_rate", MagicMock(return_value=2))

    storage = CompaniesStorage("url", 1)
    result = storage.parse_company_page(text_and_name)

    assert result["name"] == "3M Co."
    assert result["code"] == "MMM"
    assert result["price"] == 405.6
    assert result["pe"] == 19.91
    assert result["potential_profit"] == 60.15
    assert result["3M Co."] == "3M"


def test_get_index_result():
    """Tesing 'get_index_result' method."""

    storage = CompaniesStorage("url", 1)

    storage.companies = {
        "C1": {"name": "Company_1", "code": "1", "price": 100, "pe": 10},
        "C2": {"name": "Company_2", "code": "2", "price": 200, "pe": 20},
        "C3": {"name": "Company_3", "code": "3", "price": 300, "pe": 30},
    }

    price_result = storage.get_index_result("price")
    assert price_result == [
        {"name": "Company_3", "code": "3", "price": 300},
        {"name": "Company_2", "code": "2", "price": 200},
        {"name": "Company_1", "code": "1", "price": 100},
    ]

    pe_result = storage.get_index_result("pe")
    assert pe_result == [
        {"name": "Company_1", "code": "1", "pe": 10},
        {"name": "Company_2", "code": "2", "pe": 20},
        {"name": "Company_3", "code": "3", "pe": 30},
    ]
