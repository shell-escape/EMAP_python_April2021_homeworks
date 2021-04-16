from homework_1.task_4 import check_sum_of_four


def test_one_int_positive_case():
    """Testing a case with one integer in each list that satisfies the condition"""
    a, b, c, d = [0], [0], [0], [0]
    assert check_sum_of_four(a, b, c, d) == 1


def test_one_int_negative_case():
    """Testing a case with one integer in each list that does not satisfy the condition"""
    a, b, c, d = [1], [1], [1], [1]
    assert check_sum_of_four(a, b, c, d) == 0


def test_big_lists_case():
    """Testing a case with 1000 zeros in each list"""
    a, b, c, d = [[0 for _ in range(1000)] for _ in range(4)]
    assert check_sum_of_four(a, b, c, d) == 1e12
