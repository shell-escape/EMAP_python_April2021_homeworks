import pytest

from homework_8.task_2 import TableData


@pytest.fixture()
def presidents(test_data_path):
    test_filename = "example.sqlite"
    test_file_path = test_data_path.joinpath("homework_8", test_filename)
    return TableData(test_file_path, "presidents")


def test_len(presidents):
    """Testing __len__ method of TableData class"""
    presidents_len = len(presidents)

    assert presidents_len == 3


def test_getitem(presidents):
    """Testing __getitem__ method of TableData class"""
    yeltsin_row = presidents["Yeltsin"]

    assert yeltsin_row == ("Yeltsin", 999, "Russia")


def test_contains(presidents):
    """Testing __contains__ method of TableData class"""
    yeltsin_in = "Yeltsin" in presidents
    nopresident_in = "NoPresident" in presidents

    assert yeltsin_in is True
    assert nopresident_in is False


def test_iteration(presidents):
    """Testing __iter__ method of TableData class"""
    presidents_names = []
    for president in presidents:
        presidents_names.append(president[0])

    assert presidents_names == ["Yeltsin", "Trump", "Big Man Tyrone"]
