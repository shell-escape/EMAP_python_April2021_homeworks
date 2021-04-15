"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from itertools import product
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """Compute how many tuples (i, j, k, l) there are such that a[i] + b[j] + c[k] + d[l] is zero

    Args:
        a (List[int]): list of integers
        b (List[int]): list of integers
        c (List[int]): list of integers
        d (List[int]): list of integers

    Returns:
        int: the number of tuples that satisfy the condition
    """
    ab_sum, cd_sum = {}, {}
    for s in product(a, b):
        ab_sum[sum(s)] = ab_sum.get(sum(s), 0) + 1
    for s in product(c, d):
        cd_sum[sum(s)] = cd_sum.get(sum(s), 0) + 1
    return sum([ab_sum[s] * cd_sum[-s] for s in ab_sum if -s in cd_sum])
