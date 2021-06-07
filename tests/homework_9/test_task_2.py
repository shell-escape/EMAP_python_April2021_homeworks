import pytest

from homework_9.task_2 import Supressor, supressor


def test_supressors_when_should_supress():
    """Testing supressors when passed Error occurs."""
    with Supressor(IndexError):
        [][2]

    with supressor(IndexError):
        [][2]


def test_supressors_when_should_not_supress():
    """Testing supressors when not passed Error occurs."""
    with Supressor(IndexError):
        with pytest.raises(ZeroDivisionError):
            1 / 0

    with supressor(IndexError):
        with pytest.raises(ZeroDivisionError):
            1 / 0


def test_multiple_exceptions():
    """Testing supressors with multiple Errors."""
    with Supressor(IndexError, ZeroDivisionError):
        [][2]
        1 / 0

    with supressor(IndexError, ZeroDivisionError):
        [][2]
        1 / 0
