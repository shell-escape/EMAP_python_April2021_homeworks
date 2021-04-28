"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the
implementation in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""

from typing import Generator


def fizzbuzz(n: int) -> Generator:
    """Return a generator that yields first 'n' FizzBuzz numbers.

    Args:
        n: amount of FizzBuzz numbers in generator.

    Yields:
        next FizzBuzz number.

    >>> list(fizzbuzz(5))
    ['1', '2', 'fizz', '4', 'buzz']

    >>> list(fizzbuzz(15))[10:]
    ['11', 'fizz', '13', '14', 'fizzbuzz']

    """
    dividers = ((3, "fizz"), (5, "buzz"))
    for num in range(1, n + 1):
        fizzbuzz = [word for div, word in dividers if num % div == 0]
        yield "".join(fizzbuzz) if fizzbuzz else str(num)
