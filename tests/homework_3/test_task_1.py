from homework_3.task_1 import limited_cache


def test_limited_cache_on_ordinary_function():
    """Testing limited cache function using func with args and kwargs"""

    var = 1

    @limited_cache(times=2)
    def func(a, b):
        return (a, b, var)

    res_1 = func(1, b=2)

    var += 1
    res_2 = func(1, b=2)

    var += 1
    res_3 = func(1, b=2)

    assert res_1 is res_2 is res_3

    res_4 = func(1, b=2)

    assert res_1 is not res_4


def test_limited_cache_on_function_without_arguments():
    """Testing limited cache function using func without arguments"""

    var = 1

    @limited_cache(times=2)
    def func():
        return var

    res_1 = func()

    var += 1
    res_2 = func()

    var += 1
    res_3 = func()

    assert res_1 is res_2 is res_3

    res_4 = func()

    assert res_1 is not res_4
