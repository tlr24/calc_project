""" This is the main calculator program """
from calculator.history.calculations import Calculations


class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def get_last_result_value():
        """ Get the result of the last calculation"""
        return Calculations.get_calculation_last_result()

    @staticmethod
    def addition(values: tuple):
        """Adds a list of numbers"""
        Calculations.add_addition_calculation(values)
        return True

    @staticmethod
    def subtraction(values: tuple):
        """Subtracts a list of numbers"""
        Calculations.add_subtraction_calculation(values)
        return True

    @staticmethod
    def multiplication(values: tuple):
        """Multiply a list of numbers"""
        Calculations.add_multiplication_calculation(values)
        return True

    @staticmethod
    def division(values: tuple):
        """Divide a list of numbers"""
        Calculations.add_division_calculation(values)
        return True
