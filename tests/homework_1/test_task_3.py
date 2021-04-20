import pytest

from homework_1.task_3 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ("test_filename", "expected_result"),
    [
        pytest.param(
            "task_3_one_int_case.txt",
            (1, 1),
            id="A file with a single integer gives a tuple with a pair of this integer",
        ),
        pytest.param("task_3_common_case.txt", (100, -100), id="A common case"),
    ],
)
def test_find_maximum_and_minimum(test_filename, expected_result, test_data_path):
    """Testing find_maximum_and_minimum function"""
    assert (
        find_maximum_and_minimum(test_data_path.joinpath(test_filename))
        == expected_result
    )
