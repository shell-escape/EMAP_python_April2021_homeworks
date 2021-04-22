import pytest

from homework_1.task_5 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ("nums", "k", "expected_result"),
    [
        pytest.param([1, 3, -1, -3, 5, 3, 6, 7], 3, 16, id="The case from the example"),
        pytest.param([-1, 5, 5], 3, 10, id="The length of subarray with max sum < k"),
        pytest.param([-100, 0, 10, 50, 100, 0], 1, 100, id="A common case with k = 1"),
    ],
)
def test_find_maximal_subarray_sum(nums, k, expected_result):
    """Testing find_maximal_subarray_sum function"""
    assert find_maximal_subarray_sum(nums, k) == expected_result
