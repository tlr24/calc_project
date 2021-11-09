"""Test addition"""
from calculator.operations.addition import Addition


def test_addition():
    """Testing static method for addition"""
    # Arrange
    numbers = (1.0, 3.0)
    addition = Addition(numbers)
    # Act
    # Assert
    assert addition.get_result() == 4.0
