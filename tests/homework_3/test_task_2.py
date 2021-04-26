import pytest

from homework_3.task_2 import multiprocess_slow_calculate_sum, slow_calculate


def test_multiprocess_slow_calculate_sum_works_right():
    """Testing that multiprocess_slow_calculate_sum function
    gives right answer"""
    actual_sum = sum((slow_calculate(i) for i in range(5)))
    assert actual_sum == multiprocess_slow_calculate_sum(range(5))


@pytest.mark.timeout(60)
def test_multiprocess_slow_calculate_sum_works_fast():
    """Testing that multiprocess_slow_calculate_sum
    satisfies the time limit"""
    assert multiprocess_slow_calculate_sum(range(501), 167) == 1025932
