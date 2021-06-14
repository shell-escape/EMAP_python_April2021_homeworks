from homework_11.task_1 import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


def test_simplified_enum_works():
    """Tesing SimplifiedEnum metaclass works as it should."""

    assert ColorsEnum.RED == "RED"
    assert SizesEnum.XL == "XL"


def test_simplified_enum_len():
    """Testing that SimplifiedEnum metaclass
    __len__ method works right."""

    assert len(ColorsEnum) == 4
    assert len(SizesEnum) == 5


def test_simplified_enum_iter():
    """Testing that SimplifiedEnum metaclass
    __iter__ method works right."""

    colors, sizes = list(ColorsEnum), list(SizesEnum)

    assert colors == ["RED", "BLUE", "ORANGE", "BLACK"]
    assert sizes == ["XL", "L", "M", "S", "XS"]


def test_simplified_enum_warning(capsys):
    """Testing that there is a warning message when '__keys'
    attribute absent in a class."""

    class EmptyEnum(metaclass=SimplifiedEnum):
        pass

    out, _ = capsys.readouterr()

    assert out == "You should probably add '__key' attribute in your class\n"
