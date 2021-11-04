"""Test subtraction"""
from calculator.operations.subtraction import Subtraction


def test_subtraction():
    """Testing static method for subtraction"""
    # Arrange
    numbers = (5, 3.0)
    subtraction = Subtraction(numbers)
    # Act
    # Assert
    assert subtraction.get_result() == 2.0
