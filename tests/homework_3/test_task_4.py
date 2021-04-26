import pytest

from homework_3.task_4 import is_armstrong


@pytest.mark.parametrize(("number"), [0, 1, 153])
def test_is_armstrong_positive_cases(number):
    """Testing cases with actual armstong numbers"""
    assert is_armstrong(number) is True


@pytest.mark.parametrize(("number"), [10, 152])
def test_is_armstrong_negative_cases(number):
    """Testing cases with not armstong numbers"""
    assert is_armstrong(number) is False
