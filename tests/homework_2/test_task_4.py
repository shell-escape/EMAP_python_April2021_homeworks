from homework_2.task_4 import cache


def test_cache_on_func_with_args_only():
    """Testing cache function using the function from the exapmle"""

    def func(a, b):
        return (a ** b) ** 2

    cached_func = cache(func)

    arguments = (100, 200)

    first_call_result = cached_func(*arguments)
    second_call_result = cached_func(*arguments)

    assert first_call_result is second_call_result


def test_cache_on_func_with_args_and_kwargs():
    """Testing cache function using a function with args and kwargs"""

    def func(a, b, c=10, d="str"):
        return str((a ** b) ** 2) * c + d

    cached_func = cache(func)

    arguments = (100, 200, 20)

    first_call_result = cached_func(*arguments)
    second_call_result = cached_func(*arguments)

    assert first_call_result is second_call_result
