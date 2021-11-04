"""Test history calculations"""
from calculator.history.calculations import Calculations
from calculator.operations.addition import Addition


def test_add_calculation_to_history():
    """Testing adding a calculation to history"""
    values = (1, 2)
    addition = Addition(values)
    Calculations.add_calculation(addition)
    assert len(Calculations.history) == 1


def test_clear_calculations_history():
    """Testing clearing the calculations history"""
    values = (1, 2)
    addition = Addition(values)
    Calculations.history.append(addition)
    assert len(Calculations.history) == 2
    assert Calculations.clear_history() is True


def test_get_calculation():
    """Test getting a calculation from the history"""
    values = (1, 2)
    addition = Addition(values)
    Calculations.history.append(addition)
    assert Calculations.get_calculation(0).get_result() == 3


def test_count_calculations():
    """Testing getting a count of the number of calculations in calculation history"""
    Calculations.clear_history()
    values = (1, 2)
    # pylint: disable=unused-variable
    for i in range(3):
        Calculations.history.append(Addition(values))
    assert Calculations.count_calculations() == 3


def test_remove_calculation():
    """Testing removing a specific calculation"""
    Calculations.clear_history()
    numbers = (1, 1)
    addition = Addition(numbers)
    Calculations.history.append(addition)
    assert Calculations.remove_calculation(0) is True


def test_get_calculation_last():
    """Testing getting the last calculation in history"""
    Calculations.clear_history()
    numbers = (2, 1)
    numbers2 = (4, 5)
    addition = Addition(numbers)
    addition2 = Addition(numbers2)
    Calculations.history.append(addition)
    Calculations.history.append(addition2)
    assert Calculations.get_calculation_last() == addition2


def test_get_calculation_last_result():
    """Testing getting the result of the last calculation in history"""
    Calculations.clear_history()
    numbers = (2, 1)
    numbers2 = (4, 5)
    addition = Addition(numbers)
    addition2 = Addition(numbers2)
    Calculations.history.append(addition)
    Calculations.history.append(addition2)
    assert Calculations.get_calculation_last_result() == 9


def test_get_calculation_first():
    """Testing getting the first calculation in history"""
    Calculations.clear_history()
    numbers = (2, 1)
    numbers2 = (4, 5)
    addition = Addition(numbers)
    addition2 = Addition(numbers2)
    Calculations.history.append(addition)
    Calculations.history.append(addition2)
    assert Calculations.get_calculation_first() == addition


def test_get_calculation_first_result():
    """Testing getting the result of the first calculation in history"""
    Calculations.clear_history()
    numbers = (2, 1)
    numbers2 = (4, 5)
    addition = Addition(numbers)
    addition2 = Addition(numbers2)
    Calculations.history.append(addition)
    Calculations.history.append(addition2)
    assert Calculations.get_calculation_first_result() == 3
