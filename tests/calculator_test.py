""" Calculator test"""
from calculator.main import Calculator


def test_clear_history():
    """Testing clearing calculator history"""
    Calculator.add_numbers(1, 1)
    assert Calculator.clear_history() is True


def test_get_calculation():
    """Test getting a calculation from the history"""
    Calculator.add_numbers(1, 2)
    assert Calculator.get_calculation(0).get_result() == 3


def get_calculation_last():
    """Testing getting the last calculation in history"""
    Calculator.add_numbers(2, 3)
    assert Calculator.get_calculation_last().get_result == 5


def test_count_calculations():
    """Testing getting the number of calculations in history"""
    Calculator.history.clear()
    Calculator.add_numbers(2, 2)
    Calculator.subtract_numbers(2, 2)
    Calculator.multiply_numbers(2, 2)
    assert Calculator.count_calculations() == 3


def test_remove_calculation():
    """Testing removing a specific calculation"""
    Calculator.history.clear()
    Calculator.add_numbers(2, 2)
    Calculator.subtract_numbers(2, 2)
    assert Calculator.remove_calculation(1) is True


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
