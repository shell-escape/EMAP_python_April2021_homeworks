import pytest

from homework_8.task_2 import InjectionError, TableData


@pytest.fixture()
def presidents(test_data_path):
    test_filename = "example.sqlite"
    test_file_path = test_data_path.joinpath("homework_8", test_filename)
    return TableData(test_file_path, "presidents")


def test_wrong_table_name(test_data_path):
    """Tesing that InjectionError raises when table name is not valid"""
    test_filename = "example.sqlite"
    test_file_path = test_data_path.joinpath("homework_8", test_filename)

    with pytest.raises(InjectionError, match="Table name is not valid."):
        TableData(test_file_path, "DO BAD THINGS")


def test_len(presidents):
    """Testing __len__ method of TableData class"""
    presidents_len = len(presidents)

    assert presidents_len == 3


def test_getitem_positive(presidents):
    """Testing __getitem__ method of TableData class
    when the item exists"""
    yeltsin_row = presidents["Yeltsin"]

    assert tuple(yeltsin_row) == ("Yeltsin", 999, "Russia")


def test_getitem_negative(presidents):
    """Testing __getitem__ method of TableData class
    when the item does not exist"""

    with pytest.raises(ValueError, match="There is no item"):
        presidents["NotPresident"]


def test_contains(presidents):
    """Testing __contains__ method of TableData class"""
    yeltsin_in = "Yeltsin" in presidents
    notpresident_in = "NotPresident" in presidents

    assert yeltsin_in is True
    assert notpresident_in is False


def test_iteration(presidents):
    """Testing __iter__ method of TableData class"""
    presidents_names = []
    for president in presidents:
        presidents_names.append(president["name"])

    assert presidents_names == ["Yeltsin", "Trump", "Big Man Tyrone"]
