from pathlib import Path

import pytest


@pytest.fixture()
def test_data_path():
    conftest_dir_path = Path(__file__).parent
    return conftest_dir_path.joinpath("test_data")
