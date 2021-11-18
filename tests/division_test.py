"""Test division"""
import pytest
from calculator.operations.division import Division


def test_division():
    """Testing division method"""
    # Arrange
    numbers = (12, 3.0)
    division = Division(numbers)
    # Act
    # Assert
    assert division.get_result() == 4.0


def test_division_zero():
    """Testing division by zero"""
    # Arrange
    numbers = (2, 0)
    division = Division(numbers)
    # Act
    # Assert
    with pytest.raises(ZeroDivisionError):
        division.get_result()
