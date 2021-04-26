"""
Armstrong number is a number that is the sum of its own digits each
raised to the power of the number of digits.
https://en.wikipedia.org/wiki/Narcissistic_number

Examples:

- 9 is an Armstrong number, 9 = 9^1 = 9
- 10 is not: 10 != 1^2 + 0^2 = 1
- 153 is : 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153


Write a function that detects if a number is Armstrong number in
functionaly style:
 - use map or other utilities from functools library,
 - use anonymous functions (or use function as argument)
 - do not use loops, preferably using list comprehensions

"""


def is_armstrong(number: int) -> bool:
    """Check if a number is Armstrong number

    Args:
        number: a number to check

    Returns: True if 'number' is Armstrong number and False otherwise

    """
    digits = str(number)
    return sum(map(lambda x: int(x) ** len(digits), digits)) == number
