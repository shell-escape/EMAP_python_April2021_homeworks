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
        try:
            keys = attrs[f"_{class_name}__keys"]
        except KeyError:
            keys = {}
            print("You should probably add '__key' attribute in your class")  # noqa
        for key in keys:
            attrs[key] = key
        new_cls = super().__new__(cls, class_name, bases, attrs)
        new_cls._keys = keys
        return new_cls

    def __len__(cls):
        return len(cls._keys)

    def __iter__(cls):
        return iter(cls._keys)
