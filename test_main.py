"""
You can auto-discover and run all tests with this command:

    py.test

Documentation: https://docs.pytest.org/en/latest/
"""

# import the main module
from main import convert_temperature


def test_answer():
    assert convert_temperature(50) == 10.0
    assert convert_temperature(32) == 0.0
    assert convert_temperature(86) == 30.0
    assert convert_temperature(100) == 37.8
    assert convert_temperature(212) == 100.0
