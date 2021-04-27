from homework_3.task_3 import Filter, make_filter


def test_example_with_range():
    """Testing the case with even numbers in range"""
    positive_even = Filter(
        [lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)]
    )
    assert positive_even.apply(range(100)) == list(range(2, 100, 2))


def test_example_with_dicts_not_empty_result():
    """Testing the case with specified_keywords with not empty result"""
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]

    assert make_filter(name="polly", type="bird").apply(sample_data) == [sample_data[1]]


def test_example_with_dicts_empty_result():
    """Testing the case with specified_keywords with empty result"""
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]

    assert make_filter(type="bird", name="Bill").apply(sample_data) == []


def test_dict_does_not_include_key():
    """Testing the case when make_filter has keywords
    that are not in applied dicts"""

    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]

    assert make_filter(not_exist="bird", name="Bill").apply(sample_data) == []
