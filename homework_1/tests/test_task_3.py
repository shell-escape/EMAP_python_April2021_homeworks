from tempfile import NamedTemporaryFile

from homework_1.tasks.task_3 import find_maximum_and_minimum


def test_one_int_case():
    """Testing that a file with a single integer gives a tuple with a pair of this integer"""
    with NamedTemporaryFile(mode="w") as fi:
        fi.write("1")
        fi.seek(0)
        assert find_maximum_and_minimum(fi.name) == (1, 1)


def test_common_case():
    """Testing a common case"""
    with NamedTemporaryFile(mode="w") as fi:
        fi.write("1\n-100\n100\n1")
        fi.seek(0)
        assert find_maximum_and_minimum(fi.name) == (100, -100)
