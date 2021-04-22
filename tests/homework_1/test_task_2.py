import pytest

from homework_1.task_2 import check_fibonacci


@pytest.mark.parametrize(
    ("sequence", "expected_result"),
    [
        pytest.param([0], False, id="A sequence of one integer gives False"),
        pytest.param([0, 1], False, id="A sequence of two integers gives False"),
        pytest.param([0, 1, 1, 3, 5], False, id="Non-Fibonacci sequence gives False"),
        pytest.param(
            [0, 1, 1, 2, 3, 5, 8], True, id="The actual Fibonacci sequence gives True"
        ),
    ],
)
def test_check_fibonacci(sequence, expected_result):
    """Testing check_fibonacci function"""
    assert check_fibonacci(sequence) is expected_result
