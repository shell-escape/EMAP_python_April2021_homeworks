"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

# Example tree:
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


def find_occurrences(tree: dict, element: Any) -> int:
    """Find the number of occurrences of the element in the tree.

    Args:
        tree: tree to find element in.
        element: element to find.

    Returns:
        the number of occurrences.
    """
    stack = list(tree.values())
    occurrences = 0
    while stack:
        next_element = stack.pop()
        if next_element == element:
            occurrences += 1
        elif isinstance(next_element, dict):
            stack.extend(next_element.values())
        elif isinstance(next_element, (list, tuple, set)):
            stack.extend(next_element)
    return occurrences


def find_occurrences_recursive(tree: dict, element: Any) -> int:
    """Find the number of occurrences of the element in the tree.

    Args:
        tree: tree to find element in.
        element: element to find.

    Returns:
        the number of occurrences.
    """
    if tree == element:
        return 1
    if isinstance(tree, dict):
        return sum(
            find_occurrences_recursive(value, element) for value in tree.values()
        )
    if isinstance(tree, (list, set, tuple)):
        return sum(find_occurrences_recursive(el, element) for el in tree)
    return 0


if __name__ == "__main__":
    print(find_occurrences(example_tree, "RED"))  # noqa
