"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """Check if the given sequence is a Fibonacci sequence

    Args:
        data (Sequence[int]): the given sequence

    Returns:
        bool: True if data is a Fibonacci sequence and False otherwise
    """
    if len(data) == 1:
        return data[0] == 0
    if data[0] != 0 or data[1] != 1:
        return False
    for n in range(2, len(data)):
        if data[n] != data[n - 1] + data[n - 2]:
            return False
    return True
