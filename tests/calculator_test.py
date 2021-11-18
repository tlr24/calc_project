""" Calculator test"""
import pytest
from calculator.calculator import Calculator


def test_calculator_add():
    """Testing the Add function of the calc"""
    my_tuple = (1, 1)
    Calculator.add_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 2


def test_calculator_subtract():
    """Testing the subtract method of the calc"""
    my_tuple = (1, 2)
    Calculator.subtract_numbers(my_tuple)
    assert Calculator.get_last_result_value() == -1


def test_calculator_multiply():
    """Testing the multiply method of the calc"""
    my_tuple = (4, 2)
    Calculator.multiply_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 8


def test_calculator_divide():
    """Testing the divide method of the calc"""
    my_tuple = (12, 3)
    Calculator.divide_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 4


def test_calculator_divide_zero():
    """Testing the divide method of calc for zero exception"""
    my_tuple = (2, 0)
    Calculator.divide_numbers(my_tuple)
    with pytest.raises(ZeroDivisionError):
        Calculator.get_last_result_value()
