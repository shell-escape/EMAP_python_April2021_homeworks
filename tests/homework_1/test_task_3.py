from homework_1.task_3 import find_maximum_and_minimum


def test_one_int_case():
    """Testing that a file with a single integer
    gives a tuple with a pair of this integer"""
    assert find_maximum_and_minimum(
        "tests/homework_1/test_data/task_3_one_int_case.txt"
    ) == (1, 1)


def test_common_case():
    """Testing a common case"""
    assert find_maximum_and_minimum(
        "tests/homework_1/test_data/task_3_common_case.txt"
    ) == (100, -100)
