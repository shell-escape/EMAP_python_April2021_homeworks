from homework_5.task_2 import custom_sum


def test_decorated_function_works_right(capsys):
    """Testing that decorated function prints result"""
    custom_sum(1, 2, 3, 4)
    out, _ = capsys.readouterr()

    assert out == "10\n"


def test_that_doc_saved():
    """Testing than decorated function keeps the doctsting
    from original function"""
    custom_sum_doc = """This function can sum any objects which have __add___"""

    assert custom_sum.__doc__ == custom_sum_doc


def test_that_name_saved():
    """Testing than decorated function keeps the name
    from original function"""
    custom_sum_name = "custom_sum"

    assert custom_sum.__name__ == custom_sum_name


def test_that_original_func_saved():
    """Testing that decorated function keeps original function"""

    assert callable(custom_sum.__original_func)


def test_original_function_works_right(capsys):
    """Testing that saved original function does not print result"""
    without_print = custom_sum.__original_func
    without_print(1, 2, 3, 4)
    out, _ = capsys.readouterr()

    assert out == ""
