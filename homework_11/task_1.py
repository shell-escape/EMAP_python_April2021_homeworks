"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.

from enum import Enum


class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"


class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"


Should become:

class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""

from typing import Tuple


class SimplifiedEnum(type):
    """Metaclass that will add strings from '__key' attribute to the
    class attributes."""

    def __new__(cls, class_name: str, bases: Tuple[type], attrs: dict) -> type:
        for attr in attrs[f"_{class_name}__keys"]:
            attrs[attr] = attr
        return super().__new__(cls, class_name, bases, attrs)
