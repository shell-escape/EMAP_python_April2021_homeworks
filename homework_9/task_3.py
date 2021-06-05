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
    search = dir_path.rglob if walk else dir_path.glob
    files = (path for path in search(f"*{file_extension}") if path.is_file())
    for file in files:
        with open(file) as fi:
            for line in fi:
                result += len(list(tokenizer(line)))
    return result
