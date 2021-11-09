"""Test division"""
from calculator.operations.division import Division


def test_division():
    """Testing division method"""
    # Arrange
    numbers = (12, 3.0)
    division = Division(numbers)
    # Act
    # Assert
    assert division.get_result() == 4.0
