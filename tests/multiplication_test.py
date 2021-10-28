"""Test multiplication"""
from calculator.operations.multiplication import Multiplication


def test_multiplication():
    """Testing calc result is 8"""
    assert Multiplication.multiply(4, 2) == 8
