"""
Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.

Write a test that check that your function works.
Test should use Mock instead of real network interactions.

You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests

You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests


> count_dots_on_i("https://example.com/")
59

* https://docs.python.org/3/library/urllib.request.html
  #urllib.request.urlopen
"""

from urllib.request import Request, URLError, urlopen


def count_dots_on_i(url: str) -> int:
    """Count 'i' letters presented in HTML by 'url'.

    Args:
        url: URL

    Raises:
        ValueError: if URL is unreachable.

    Returns:
        The number of 'i' letters.
    """
    try:
        req = Request(url)
        i_count = 0
        with urlopen(req) as html:  # noqa
            for line in html:
                i_count += str(line).count("i")
            return i_count
    except URLError:
        raise ValueError(f"Unreachable {url}")
