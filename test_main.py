"""
You can auto-discover and run all tests with this command:

    py.test

Documentation: https://docs.pytest.org/en/latest/
"""

# import the main module
from main import main


def test_answer():
    assert main() == 'Hello World!'
