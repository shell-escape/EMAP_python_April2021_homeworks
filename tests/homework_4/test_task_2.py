from io import StringIO
from unittest.mock import MagicMock
from urllib.request import URLError

import pytest

from homework_4.task_2_mock_input import count_dots_on_i


def test_unreachable_url(monkeypatch):
    """Testing than ValueError raises when URL is unreachable
    using mock"""
    mock = MagicMock()
    mock.side_effect = URLError(404)
    monkeypatch.setattr("homework_4.task_2_mock_input.Request", mock)
    with pytest.raises(ValueError, match="Unreachable"):
        count_dots_on_i(mock)


def test_common_case(monkeypatch):
    """Testing common case using mock"""
    content = "There are severals 'i' letters here\niii"
    mock = MagicMock(return_value=StringIO(content))
    monkeypatch.setattr("homework_4.task_2_mock_input.Request", mock)
    monkeypatch.setattr("homework_4.task_2_mock_input.urlopen", mock)
    result = count_dots_on_i("it doesn't matter what is here")
    assert mock.call_count == 2
    assert result == 4
