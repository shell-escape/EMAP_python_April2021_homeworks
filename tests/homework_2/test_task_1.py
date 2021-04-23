import pytest

from homework_2.task_1 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)


@pytest.mark.parametrize(
    ("test_filename", "expected_result"),
    [
        pytest.param(
            "task_1_file_with_short_text.txt",
            ["charactersß", "string", "fuünny", "withéé", "ààa"],
            id="Testing on the file with short text",
        ),
    ],
)
def test_get_longest_diverse_words(test_filename, expected_result, test_data_path):
    """Testing get_longest_diverse_words function"""
    test_file_path = test_data_path.joinpath(test_filename)
    assert get_longest_diverse_words(test_file_path) == expected_result


@pytest.mark.parametrize(
    ("test_filename", "expected_result"),
    [
        pytest.param(
            "task_1_file_with_short_text.txt",
            "\n",
            id="The line break symbol is the rarest and first in byte value order",
        ),
    ],
)
def test_get_rarest_char(test_filename, expected_result, test_data_path):
    """Testing get_rarest_char function"""
    test_file_path = test_data_path.joinpath(test_filename)
    assert get_rarest_char(test_file_path) == expected_result


@pytest.mark.parametrize(
    ("test_filename", "expected_result"),
    [
        pytest.param(
            "task_1_file_with_short_text.txt",
            1,
            id="The dot symbol is the only punctuation symbol in the file",
        ),
    ],
)
def test_count_punctuation_chars(test_filename, expected_result, test_data_path):
    """Testing count_punctuation_chars function"""
    test_file_path = test_data_path.joinpath(test_filename)
    assert count_punctuation_chars(test_file_path) == expected_result


@pytest.mark.parametrize(
    ("test_filename", "expected_result"),
    [
        pytest.param(
            "task_1_file_with_short_text.txt",
            6,
            id="The file contains 6 non-ascii symbols",
        ),
    ],
)
def test_count_non_ascii_chars(test_filename, expected_result, test_data_path):
    """Testing count_non_ascii_chars function"""
    test_file_path = test_data_path.joinpath(test_filename)
    assert count_non_ascii_chars(test_file_path) == expected_result


@pytest.mark.parametrize(
    ("test_filename", "encoding", "expected_result"),
    [
        pytest.param(
            "task_1_file_with_short_text.txt",
            None,
            "à",
            id="'à' is the most common non-ascii acharacter and first by byte value",
        ),
        pytest.param(
            "data_piece.txt",
            "unicode_escape",
            "\u2014",
            id="'à'",
        ),
    ],
)
def test_get_most_common_non_ascii_char(
    test_filename, encoding, expected_result, test_data_path
):
    """Testing get_most_common_non_ascii_char function"""
    test_file_path = test_data_path.joinpath(test_filename)
    assert get_most_common_non_ascii_char(test_file_path, encoding) == expected_result
