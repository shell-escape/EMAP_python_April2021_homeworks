"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g')
    == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p')
    == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2)
    == ['p', 'n', 'l', 'j', 'h']

"""

from typing import Any, Iterable, List


def custom_range(
    values: Iterable[Any], first_border: Any, second_border: Any = None, step: int = 1
) -> List[Any]:
    """Universal range function.

    Args:
        values: iterable object
        first_border: end of range in second_border is None
                      and start of range otherwise
        second_border: end of range
        step: step of range

    Returns:
        list of elements in required range
    """

    list_of_values = list(values)

    if second_border is None:
        start = 0
        stop = list_of_values.index(first_border)
    else:
        start = list_of_values.index(first_border)
        stop = list_of_values.index(second_border)

    return list_of_values[start:stop:step]
