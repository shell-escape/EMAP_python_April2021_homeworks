import pytest

from homework_1.sample_project.calculator.calc import check_power_of_2


@pytest.mark.parametrize(
    ("number", "expected_result"),
    [
        pytest.param(65536, True, id="Actual power of 2 gives True"),
        pytest.param(12, False, id="Non-power of 2 gives False"),
        pytest.param(0, False, id="Zero gives False"),
    ],
)
def test_check_power_of_2(number, expected_result):
    """Testing check_power_of_2 function"""
    assert check_power_of_2(number) is expected_result
