from homework_9.task_1 import merge_sorted_files


def test_one_file_one_digit(test_data_path):
    """Testing merge_sorted_files function on one
    file of one digit."""
    test_filename = "task_1_sorted_file_3.txt"
    test_file_path = test_data_path.joinpath("homework_9", test_filename)
    sorted_list = list(merge_sorted_files([test_file_path]))

    assert sorted_list == [100]


def test_one_file(test_data_path):
    """Testing merge_sorted_files function on one file."""
    test_filename = "task_1_sorted_file_1.txt"
    test_file_path = test_data_path.joinpath("homework_9", test_filename)
    sorted_list = list(merge_sorted_files([test_file_path]))

    assert sorted_list == [1, 3, 5]


def test_common_case(test_data_path):
    """Testing merge_sorted_files on common case."""
    test_filenames = [
        "task_1_sorted_file_1.txt",
        "task_1_sorted_file_2.txt",
        "task_1_sorted_file_3.txt",
    ]
    test_file_paths = [
        test_data_path.joinpath("homework_9", test_filename)
        for test_filename in test_filenames
    ]
    sorted_list = list(merge_sorted_files(test_file_paths))

    assert sorted_list == [1, 2, 3, 5, 6, 8, 10, 100]
