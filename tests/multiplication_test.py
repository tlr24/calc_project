"""Test multiplication"""
from calculator.operations.multiplication import Multiplication


def test_multiplication():
    """Testing static method for multiplication"""
    # Arrange
    numbers = (2, 6.0)
    multiplication = Multiplication(numbers)
    # Act
    # Assert
    assert multiplication.get_result() == 12.0
