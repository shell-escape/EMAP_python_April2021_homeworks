"""
Write a function that takes a number N as an input and returns
N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.

That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...


Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions


> fizzbuzz(5)
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15,
   "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """Returns first 'n' FizzBuzz numbers.

    Args:
        n: amount of FizzBuzz numbers to return.

    Returns:
        list with FizzBuzz numbers.

    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']

    >>> fizzbuzz(15)[10:]
    ['11', 'fizz', '13', '14', 'fizzbuzz']

    How to run doctests:
    - Install Python 3.8 (https://www.python.org/downloads/)
    - Install pytest `pip install pytest`
    - Clone the repository
      <https://github.com/shell-escape/EMAP_python_April2021_homeworks>
    - Checkout branch <homework_4> if it exists else stay in master
    - Open terminal
    - Go to repository folder
    - Run
        $ pytest --doctest-modules "homework_4/task_4_doctest.py"
      or just
        $ pytest "homework_4/task_4_doctest.py"
      if "--doctest-modules" is in pytest.ini file
      in the root of repository
    """

    fizzbuzz_numbers = []
    dividers = ((3, "fizz"), (5, "buzz"))
    for num in range(1, n + 1):
        fizzbuzz = [word for divider, word in dividers if num % divider == 0]
        fizzbuzz_numbers.append("".join(fizzbuzz) if fizzbuzz else str(num))
    return fizzbuzz_numbers
