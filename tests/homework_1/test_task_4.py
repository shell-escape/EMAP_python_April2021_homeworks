import pytest

from homework_1.task_4 import check_sum_of_four


@pytest.mark.parametrize(
    ("a", "b", "c", "d", "expected_result"),
    [
        pytest.param(
            [0],
            [0],
            [0],
            [0],
            1,
            id="One integer in each list that can be summed to zero",
        ),
        pytest.param(
            [1],
            [1],
            [1],
            [1],
            0,
            id="One integer in each list that cannot be summed to zero",
        ),
        pytest.param(
            *[[0 for _ in range(1000)] for _ in range(4)],
            1e12,
            id="The case with 1000 zeros in each list",
        ),
    ],
)
def test_check_sum_of_four(a, b, c, d, expected_result):
    """Testing check_sum_of_four function"""
    assert check_sum_of_four(a, b, c, d) == expected_result
