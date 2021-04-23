from string import ascii_lowercase

from homework_2.task_5 import custom_range


def test_only_start():
    """Testing the function when only first border provided"""
    assert custom_range(ascii_lowercase, "g") == ["a", "b", "c", "d", "e", "f"]


def test_start_and_end():
    """Testing the function when both borders provided"""
    expected_result = ["g", "h", "i", "j", "k", "l", "m", "n", "o"]
    assert custom_range(ascii_lowercase, "g", "p") == expected_result


def test_negative_step():
    """Testing the function when step is negitive"""
    assert custom_range(ascii_lowercase, "p", "g", -2) == ["p", "n", "l", "j", "h"]
