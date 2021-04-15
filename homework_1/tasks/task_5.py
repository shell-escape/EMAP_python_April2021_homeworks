"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """Find a sub-array with length less equal to "k", with maximal sum.
    Based on Kadane's algorithm [https://en.wikipedia.org/wiki/Maximum_subarray_problem]"""
    best_sum = float("-inf")
    current_sum = 0
    for current_end, num in enumerate(nums):
        if current_sum <= 0:
            # Start a new sequence at the current element
            current_start = current_end
            current_sum = num
        else:
            # Extend the existing sequence with the current element
            current_sum += num

        if current_end - current_start == k:
            # restrict the length of sub-array
            current_sum -= nums[current_start]
            current_start += 1

        if current_sum > best_sum:
            best_sum = current_sum

    return best_sum
