""" Calculator test"""
from calculator.main import Calculator


def test_calculator_add_static():
    """testing calc result"""
    assert Calculator.add_numbers(1, 2) == 3


def test_calculator_add():
    """Testing the Add function of the calc"""
    # Arrange by instantiating the calc class
    calc = Calculator()
    # Act by calling the method to be tested
    result_value = calc.add_numbers(1, 1)
    # Assert that the results are correct
    assert result_value == 2


def test_calculator_subtract():
    """Testing the subtract method of the calc"""
    calc = Calculator()
    calc.subtract_numbers(1, 2)
    assert calc.subtract_numbers(1, 2) == -1


def test_calculator_multiply():
    """Testing the multiply method of the calc"""
    calc = Calculator()
    calc.multiply_numbers(4, 2)
    assert calc.multiply_numbers(4, 2) == 8


def test_calculator_divide():
    """Testing the divide method of the calc"""
    calc = Calculator()
    calc.divide_numbers(12, 3)
    assert calc.divide_numbers(12, 3) == 4


def test_calculator_divide_zero():
    """Testing the divide method of calc for zero exception"""
    calc = Calculator()
    calc.divide_numbers(2, 0)
    assert calc.divide_numbers(2, 0) is None
