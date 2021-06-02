"""
Write a function that takes directory path, a file extension and an
optional tokenizer.
It will count lines in all files with that extension if there are no
tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
> universal_file_counter(test_dir, "txt")
6
> universal_file_counter(test_dir, "txt", str.split)
6

"""
import os
from pathlib import Path
from typing import Callable


def universal_file_counter(
    dir_path: Path,
    file_extension: str,
    tokenizer: Callable = None,
    walk: bool = False,
) -> int:
    """Count the number of tokens produced by a passed tokenizer
    in a passed directory files with a passed extension. If tokenizer is
    not provided, count the number of lines.

    Args:
        dir_path: a directory to count tokens in its files.
        file_extension: file extension.
        tokenizer: tokenizer.
        walk: whether to count files in nested directories.

    Returns:
        the number of tokens in corresponding files.
    """
    result = 0
    tokenizer = tokenizer or (lambda line: (line,))
    for root, _, files in os.walk(dir_path):
        filtered_files = [file for file in files if file.endswith(file_extension)]
        for file in filtered_files:
            with open(os.path.join(root, file)) as fi:
                for line in fi:
                    result += len(list(tokenizer(line)))
        if not walk:
            break
    return result
