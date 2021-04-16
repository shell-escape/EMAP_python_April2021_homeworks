"""
Write down the function, which reads input line-by-line, and
    find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.
"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """Find maximum and minimum values in a file

    Args:
        file_name: name of the file

    Returns:
        tuple with the maximum and minimum values
    """
    max_number, min_number = float("-inf"), float("inf")
    with open(file_name) as fi:
        for line in fi:
            max_number = max(max_number, int(line))
            min_number = min(min_number, int(line))
    return (max_number, min_number)
