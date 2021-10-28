"""Test division"""
from calculator.operations.division import Division


def test_division():
    """Testing calc result is 8"""
    assert Division.divide(12, 2) == 6
