"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    """Return a function that behaves like 'func' but cache it.
    I.e. if 'args' and 'kwargs' were called before -
    returns a result from cache.

    Args:
        func (Callable): a function to cache

    Returns:
        Callable: cached function
    """
    cache_storage = {}

    def wrapped(*args, **kwargs) -> Any:
        """Accepts 'args' and 'kwargs' and calls 'func' or takes
        result from cache.

        Returns:
            'func' returned value.
        """
        str_args = f"{args}, {kwargs}"

        if str_args not in cache_storage:
            cache_storage[str_args] = func(*args, **kwargs)

        return cache_storage[str_args]

    return wrapped
