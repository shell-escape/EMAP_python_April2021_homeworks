from tempfile import NamedTemporaryFile

import pytest

from homework_4.task_1_read_file import read_magic_number


def test_not_existing_file():
    """Testing that read_magic_number function raises ValueError
    when given by 'path' file does not exist"""
    with pytest.raises(ValueError, match="The file does not exist"):
        read_magic_number("Not_existing_file.txt")


def test_empty_file():
    """Testing that read_magic_number function raises ValueError
    when given by 'path' file is empty"""
    with NamedTemporaryFile(mode="w") as fi:
        with pytest.raises(ValueError, match="The first line is not a number"):
            read_magic_number(fi.name)


def test_file_with_bad_first_line():
    """Testing that read_magic_number function raises ValueError
    when the first line of given by 'path' file can not be converted
    to a number"""
    with NamedTemporaryFile(mode="w") as fi:
        fi.write("not_a_number")
        fi.seek(0)
        with pytest.raises(ValueError, match="The first line is not a number"):
            read_magic_number(fi.name)


@pytest.mark.parametrize(
    ("file_content"),
    [
        "1",
        "1.0",
        "2.5\nnot_a_number",
    ],
)
def test_positive_cases(file_content):
    """Testing that read_magic_number function gives True if the
    number"""
    with NamedTemporaryFile(mode="w") as fi:
        fi.write(file_content)
        fi.seek(0)
        assert read_magic_number(fi.name) is True


@pytest.mark.parametrize(
    ("file_content"),
    [
        "3",
        "3.0",
        "0.999",
    ],
)
def test_negative_cases(file_content):
    """Testing that read_magic_number function gives True if the
    number"""
    with NamedTemporaryFile(mode="w") as fi:
        fi.write(file_content)
        fi.seek(0)
        assert read_magic_number(fi.name) is False
