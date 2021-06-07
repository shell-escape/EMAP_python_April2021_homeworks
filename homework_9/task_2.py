"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

> with supressor(IndexError):
...    [][2]

"""

from contextlib import contextmanager


class Supressor:
    """A context manager that supresses passed exception.

    Args:
        exception: exception to supress.

    Attributes:
        exception: exception to supress.
    """

    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        return exc_type in self.exceptions


@contextmanager
def supressor(*exceptions):
    """A context manager that supresses passed exception.

    Args:
        exception: exception to supress.
    """
    try:
        yield
    except exceptions:
        pass
