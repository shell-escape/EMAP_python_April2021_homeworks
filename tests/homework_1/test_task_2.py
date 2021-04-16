from homework_1.task_2 import check_fibonacci


def test_one_int_case():
    """Testing that data with only one integer give False"""
    assert not check_fibonacci([0])


def test_two_int_case():
    """Testing that data with only two integers give False"""
    assert not check_fibonacci([0, 1])


def test_negative_case():
    """Testing that not Fibonacci sequence gives False"""
    assert not check_fibonacci([0, 1, 1, 3, 5])


def test_positive_case():
    """Testing that actual Fibonacci sequence gives True"""
    assert check_fibonacci([0, 1, 1, 2, 3])
