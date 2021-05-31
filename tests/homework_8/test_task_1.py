import pytest

from homework_8.task_1 import KeyValueStorage, ParserError


def test_positive_case(test_data_path):
    """Testing KeyValueStorage class with the case from the example."""
    test_filename = "task_1_positive_case.txt"
    test_file_path = test_data_path.joinpath("homework_8", test_filename)
    storage = KeyValueStorage(test_file_path)

    assert storage.name == "kek"
    assert storage.last_name == "top"
    assert storage.song_name == "shadilay"
    assert storage.power == 9001


def test_negative_case(test_data_path):
    """Testing that KeyValueStorage initializer raises ValueError when
    keyword can not be attribute name"""
    test_filename = "task_1_negative_case.txt"
    test_file_path = test_data_path.joinpath("homework_8", test_filename)

    with pytest.raises(ValueError, match="Value cannot be assigned to an attribute."):
        KeyValueStorage(test_file_path)


def test_parser_error(test_data_path):
    """Testing that ParserError raises when file contains wrong number
    of '=' sign in any line."""
    test_filename = "task_1_error_case.txt"
    test_file_path = test_data_path.joinpath("homework_8", test_filename)

    with pytest.raises(ParserError, match="Each line must contain only one '=' sign."):
        KeyValueStorage(test_file_path)
