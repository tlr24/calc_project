""" This is the main calculator program """
from calculator.history.calculations import Calculations


class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def get_last_result_value():
        """ Get the result of the last calculation"""
        return Calculations.get_calculation_last_result()

    @staticmethod
    def add_numbers(tuple_values: tuple):
        """Adds a list of numbers"""
        Calculations.add_addition_calculation(tuple_values)
        return True

    @staticmethod
    def subtract_numbers(tuple_values: tuple):
        """Subtracts a list of numbers"""
        Calculations.add_subtraction_calculation(tuple_values)
        return True

    @staticmethod
    def multiply_numbers(tuple_values: tuple):
        """Multiply a list of numbers"""
        Calculations.add_multiplication_calculation(tuple_values)
        return True

    @staticmethod
    def divide_numbers(tuple_values: tuple):
        """Divide a list of numbers"""
        Calculations.add_division_calculation(tuple_values)
        return True
