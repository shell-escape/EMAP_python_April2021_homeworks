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
from pathlib import Path
from typing import Generator, List, Union


def file_gen(filename: Union[Path, str]) -> Generator[int, None, None]:
    """Generator for one integer in line file reading.

    Args:
        filename: path to a file with one integer in line.

    Yields:
        next integer.
    """
    with open(filename) as file:
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
    gens = [file_gen(file) for file in file_list]
    priority_queue = [(next(gen), i) for i, gen in enumerate(gens)]
    while priority_queue:
        next_element, index = heapq.heappop(priority_queue)
        yield next_element
        try:
            heapq.heappush(priority_queue, (next(gens[index]), index))
        except StopIteration:
            continue
