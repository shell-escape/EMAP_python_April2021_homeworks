"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values, compute how many tuples
    (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same
    length of N where 0 ≤ N ≤ 1000.
"""
from collections import Counter
from itertools import product
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """Compute how many tuples (i, j, k, l) there are such that
       a[i] + b[j] + c[k] + d[l] is zero

    Args:
        a: list of integers
        b: list of integers
        c: list of integers
        d: list of integers

    Returns:
        the number of tuples that satisfy the condition
    """
    ab_sums = Counter(sum(pair) for pair in product(a, b))
    cd_sums = Counter(sum(pair) for pair in product(c, d))
    return sum([ab_sums[s] * cd_sums[-s] for s in ab_sums if -s in cd_sums])
