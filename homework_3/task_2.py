"""
Here's a not very efficient calculation function
that calculates something important:"""

import hashlib
import random
import struct
import time
from multiprocessing import Pool
from typing import Iterable


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))  # noqa
    data = hashlib.md5(str(value).encode()).digest()  # noqa
    return sum(struct.unpack("<" + "B" * len(data), data))


"""
Calculate total sum of slow_calculate() of all numbers starting
from 0 to 500. Calculation time should not take more than a minute.
Use functional capabilities of multiprocessing module.
You are not allowed to modify slow_calculate function.
"""


def multiprocess_slow_calculate_sum(
    values: Iterable[int], processes_number: int = None
) -> int:
    """Sum of slow_calculate function of 'iterable' objects
    using 'processes_number' processes.

    Args:
        values: values for slow_calculate to sum
        processes_number: the number of processes

    Returns:
        Sum of slow_calculate function of values
    """
    with Pool(processes_number) as p:
        return sum(p.map(slow_calculate, values))
