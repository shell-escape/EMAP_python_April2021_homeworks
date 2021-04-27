"""
In previous homework task 4, you wrote a cache function that
remembers other function output value. Modify it to be a parametrized
decorator, so that the following code::

    @cache(times=3)
    def some_function():
        pass


Would give out cached value up to `times` number only.
Example::

    @cache(times=2)
    def f():
    # careful with input() in python2, use raw_input() instead
        return input('? ')

    > f()
    ? 1
    '1'
    > f()     # will remember previous value
    '1'
    > f()     # but use it up to two times only
    '1'
    > f()
    ? 2
    '2'
"""

from dataclasses import dataclass
from typing import Any, Callable


def limited_cache(times: int) -> Callable:
    """Returns a decorator that cache values up to 'times' number.

    Args:
        times: the number of times to cache function

    Returns:
        parametrized decorator
    """

    def cache(func: Callable) -> Callable:
        """Return a function that behaves like 'func' but cache it.
        I.e. if 'args' and 'kwargs' were called before -
        returns a result from cache.

        Args:
            func: a function to cache

        Returns:
            cached function
        """

        @dataclass
        class FunctionData:
            """Dataclass to store cached function result
            and count times that function was called"""

            __slots__ = ("result", "counter")
            result: Any
            counter: int

        cache_and_counter = {}

        def wrapped(*args, **kwargs) -> Any:
            """Accepts 'args' and 'kwargs' and calls 'func' or takes
            result from cache.

            Returns:
                'func' returned value.
            """
            str_args = f"{args}, {kwargs}"

            if str_args in cache_and_counter:
                cache_and_counter[str_args].counter -= 1
                if cache_and_counter[str_args].counter == 0:
                    del cache_and_counter[str_args]

            if str_args not in cache_and_counter:
                cache_and_counter[str_args] = FunctionData(
                    func(*args, **kwargs), times + 1
                )

            return cache_and_counter[str_args].result

        return wrapped

    return cache
