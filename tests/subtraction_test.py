"""Test subtraction"""
from calculator.operations.subtraction import Subtraction


def test_subtraction():
    """Testing calc result is -1"""
    assert Subtraction.subtract(1, 2) == -1
