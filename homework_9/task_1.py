"""
Write a function that merges integer from sorted files and
returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
import heapq
from contextlib import ExitStack
from pathlib import Path
from typing import Generator, List, Union


def file_gen(file: Union[Path, str]) -> Generator[int, None, None]:
    """Generator that yiels integers from file that contains
    one integer in line.

    Args:
        file: a file to yield integers from.

    Yields:
        next integer.
    """
    for line in file:
        yield int(line)


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Generator[int, None, None]:
    """Generator that yields integers from sorted files in sorted order.

    Args:
        file_list: list of paths to sorted files.
                   Files should contain one integer per line.

    Yields:
        next integer in sorted order.
    """
    with ExitStack() as stack:
        files = [stack.enter_context(open(filename)) for filename in file_list]
        gens = [file_gen(file) for file in files]
        yield from heapq.merge(*gens)
