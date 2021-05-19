"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: s = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""
from itertools import zip_longest
from typing import Generator


def clear_reversed(string: str) -> Generator:
    """Generator for backspace string compare.

    Args:
        string: any string.

    Yields:
        not backspaced characters in reversed order.
    """
    skip = False
    for char in reversed(string):
        if char == "#":
            skip = True
            continue
        if not skip:
            yield char
        skip = False


def backspace_compare(first: str, second: str) -> bool:
    """Compare two string after backspacing.
    '#' means a backspace character.

    Args:
        first: string with backspaces.
        second: string with backspaces.

    Returns:
        Whether the strings are equal after backspacing.

    >>> backspace_compare("###", "")
    True

    >>> backspace_compare("ab#c", "ad#c")
    True

    >>> backspace_compare("a##c", "#a#c")
    True

    >>> backspace_compare("a#c", "b")
    False

    >>> backspace_compare("qb#c", "zd#c")
    False
    """
    first_cleared = clear_reversed(first)
    second_cleared = clear_reversed(second)

    for char_first, char_second in zip_longest(first_cleared, second_cleared):
        if char_first != char_second:
            return False
    return True
