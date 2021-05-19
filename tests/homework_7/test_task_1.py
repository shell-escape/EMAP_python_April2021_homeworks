from homework_7.task_1 import find_occurrences


def test_empty_tree():
    """Testing that there are no occurrences in an empty tree."""
    empty_tree = {}
    occurrences = find_occurrences(empty_tree, "smth")

    assert occurrences == 0


def test_example():
    """Testing find_occurrences() with the tree from the example."""
    example_tree = {
        "first": ["RED", "BLUE"],
        "second": {
            "simple_key": ["simple", "list", "of", "RED", "valued"],
        },
        "third": {
            "abc": "BLUE",
            "jhl": "RED",
            "complex_key": {
                "key1": "value1",
                "key2": "RED",
                "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
            },
        },
        "fourth": "RED",
    }
    occurrences = find_occurrences(example_tree, "RED")

    assert occurrences == 6


def test_element_is_list():
    """Testing find_occurrences() when sought element is list"""
    tree = {
        "first": ["RED", "BLUE"],
        "second": {
            "simple_key": ["RED", "BLUE"],
        },
        "third": {
            "abc": "BLUE",
            "jhl": "RED",
            "complex_key": {
                "key1": "value1",
                "key2": "RED",
                "key3": ["a", "lot", "of", "values", {"nested_key": ["RED", "BLUE"]}],
            },
        },
        "fourth": "RED",
    }
    occurrences = find_occurrences(tree, ["RED", "BLUE"])

    assert occurrences == 3


def test_element_is_dict():
    """Testing find_occurrences() when sought element is list"""
    tree = {
        "first": {"nested_key": "RED"},
        "second": {
            "simple_key": {"nested_key": "RED"},
        },
        "third": {
            "abc": {"nested_key": "RED"},
            "jhl": "RED",
            "complex_key": {
                "key1": "value1",
                "key2": "RED",
                "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
            },
        },
        "fourth": "RED",
    }
    occurrences = find_occurrences(tree, {"nested_key": "RED"})

    assert occurrences == 4
