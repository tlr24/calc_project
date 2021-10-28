""" Calculator test"""
from calculator.main import Calculator


def test_calculator_add():
    """Testing the Add function of the calc"""
    assert Calculator.add_numbers(1, 1) == 2


def test_calculator_subtract():
    """Testing the subtract method of the calc"""
    assert Calculator.subtract_numbers(1, 2) == -1


def test_calculator_multiply():
    """Testing the multiply method of the calc"""
    assert Calculator.multiply_numbers(4, 2) == 8


def test_calculator_divide():
    """Testing the divide method of the calc"""
    assert Calculator.divide_numbers(12, 3) == 4


def test_calculator_divide_zero():
    """Testing the divide method of calc for zero exception"""
    assert Calculator.divide_numbers(2, 0) is None
