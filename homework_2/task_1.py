"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount
    of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from string import printable, punctuation
from typing import List


def get_longest_diverse_words(file_path: str, encoding: str = None) -> List[str]:
    """Find 10 longest words consisting from largest amount
    of unique symbols (in lexicographic order).

    Args:
        file_path: path to a file
        encoding: the name of the encoding

    Returns:
        list with 10 corresponding words
    """
    with open(file_path, encoding=encoding) as fi:
        text = fi.read().lower()
    cleaned_text = "".join(char for char in text if char not in punctuation)
    words = cleaned_text.split()

    def key_for_longest_unique(word):
        return (-len(set(word)), -len(word), word)

    return sorted(words, key=key_for_longest_unique)[:10]


def get_rarest_char(file_path: str, encoding: str = None) -> str:
    """Find the rarest character in a file (in byte value order).

    Args:
        file_path: path to a file
        encoding: the name of the encoding

    Returns:
        the rarest character
    """
    char_counter = {}
    with open(file_path, encoding=encoding) as fi:
        for line in fi:
            for char in line:
                if char in printable:
                    char_counter[char] = char_counter.get(char, 0) + 1
    return min(char_counter, key=lambda char: (char_counter[char], char))


def count_punctuation_chars(file_path: str, encoding: str = None) -> int:
    """Count punctuation characters in a file.

    Args:
        file_path: path to a file
        encoding: the name of the encoding

    Returns:
        the number of punctuation chars
    """
    punctuation_counter = 0
    with open(file_path, encoding=encoding) as fi:
        for line in fi:
            for char in line:
                if char in punctuation:
                    punctuation_counter += 1
    return punctuation_counter


def count_non_ascii_chars(file_path: str, encoding: str = None) -> int:
    """Count every non-ascii characters.

    Args:
        file_path: path to a file
        encoding: the name of the encoding

    Returns:
        the number of non ascii characters
    """
    non_ascii_counter = 0
    with open(file_path, encoding=encoding) as fi:
        for line in fi:
            for char in line:
                if ord(char) > 128:
                    non_ascii_counter += 1
    return non_ascii_counter


def get_most_common_non_ascii_char(file_path: str, encoding: str = None) -> str:
    """Find the most common non-ascii character in a file
    (in byte value order).

    Args:
        file_path: path to a file
        encoding: the name of the encoding

    Returns:
        the most common non-ascii symbol
    """
    non_ascii_counter = {}
    with open(file_path, encoding=encoding) as fi:
        for line in fi:
            for char in line:
                if ord(char) > 128:
                    non_ascii_counter[char] = non_ascii_counter.get(char, 0) + 1

    def key_for_max(char):
        return (non_ascii_counter[char], -ord(char))

    return max(non_ascii_counter, key=key_for_max)


if __name__ == "__main__":
    data_longest_words = get_longest_diverse_words(
        "data.txt", encoding="unicode_escape"
    )

    data_rarest_char = get_rarest_char("data.txt", encoding="unicode_escape")

    data_punctuation_count = count_punctuation_chars(
        "data.txt", encoding="unicode_escape"
    )

    data_non_ascii_count = count_non_ascii_chars("data.txt", encoding="unicode_escape")

    data_most_common_non_ascii_char = get_most_common_non_ascii_char(
        "data.txt", encoding="unicode_escape"
    )
    """
    data_longest_words:
    ['unmißverständliche', 'werkstättenlandschaft',
    'werkstättenlandschaft', 'bevölkerungsabschub',
    'kollektivschuldiger', 'politischstrategischen',
    'millionenbevölkerung', 'résistancebewegungen',
    'friedensabstimmung', 'selbstverständlich']

    data_rarest_char:
    "("

    data_punctuation_count:
    5305

    data_non_ascii_count:
    2972

    data_most_common_non_ascii_char:
    ä
    """
