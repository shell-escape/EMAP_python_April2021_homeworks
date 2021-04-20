from homework_1.task_5 import find_maximal_subarray_sum


def test_example_case():
    """Testing the case from the example"""
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    assert find_maximal_subarray_sum(nums, k) == 16


def test_less_k_case():
    """Testing a case where length of sub-array with max sum < k"""
    nums = [-1, 5, 5]
    k = 3
    assert find_maximal_subarray_sum(nums, k) == 10


def test_k_is_one_case():
    """Testing a common case with k = 1"""
    nums = [-100, 0, 10, 50, 100, 0]
    k = 1
    assert find_maximal_subarray_sum(nums, k) == 100
