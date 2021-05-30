from homework_7.task_1 import find_occurrences, find_occurrences_recursive


def test_empty_tree():
    """Testing that there are no occurrences in an empty tree."""
    empty_tree = {}
    occurrences_stack = find_occurrences(empty_tree, "smth")
    occurrences_recursive = find_occurrences_recursive(empty_tree, "smth")

    assert occurrences_stack == 0
    assert occurrences_recursive == 0


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
    occurrences_stack = find_occurrences(example_tree, "RED")
    occurrences_recursive = find_occurrences_recursive(example_tree, "RED")

    assert occurrences_stack == 6
    assert occurrences_recursive == 6


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
    occurrences_stack = find_occurrences(tree, ["RED", "BLUE"])
    occurrences_recursive = find_occurrences_recursive(tree, ["RED", "BLUE"])

    assert occurrences_stack == 3
    assert occurrences_recursive == 3


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
    occurrences_stack = find_occurrences(tree, {"nested_key": "RED"})
    occurrences_recursive = find_occurrences_recursive(tree, {"nested_key": "RED"})

    assert occurrences_stack == 4
    assert occurrences_recursive == 4
