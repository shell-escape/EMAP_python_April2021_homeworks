from homework_9.task_3 import universal_file_counter


def test_with_default_tokenizer_not_nested_dir(test_data_path):
    """Testing universal_file_counter function when tokenizer
    is not provided and 'walk' parameter is False.
    """
    test_dirname = "task_3_test_dir"
    test_dir_path = test_data_path.joinpath("homework_9", test_dirname)
    result = universal_file_counter(test_dir_path, ".txt")

    assert result == 6


def test_with_default_tokenizer_nested_dir(test_data_path):
    """Testing universal_file_counter function when tokenizer
    is not provided and 'walk' parameter is True.
    """
    test_dirname = "task_3_test_dir"
    test_dir_path = test_data_path.joinpath("homework_9", test_dirname)
    result = universal_file_counter(test_dir_path, ".txt", walk=True)

    assert result == 10


def test_with_tokenizer_not_nested_dir(test_data_path):
    """Testing universal_file_counter function when tokenizer
    is provided and 'walk' parameter is False.
    """
    test_dirname = "task_3_test_dir"
    test_dir_path = test_data_path.joinpath("homework_9", test_dirname)
    tokenizer = str.split
    result = universal_file_counter(test_dir_path, ".txt", tokenizer)

    assert result == 8


def test_with_tokenizer_nested_dir(test_data_path):
    """Testing universal_file_counter function when tokenizer
    is provided and 'walk' parameter is True.
    """
    test_dirname = "task_3_test_dir"
    test_dir_path = test_data_path.joinpath("homework_9", test_dirname)
    tokenizer = str.split
    result = universal_file_counter(test_dir_path, ".txt", tokenizer, walk=True)

    assert result == 12
