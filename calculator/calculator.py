""" This is the main calculator program """
from calculator.operations.addition import Addition
from calculator.operations.subtraction import Subtraction
from calculator.operations.multiplication import Multiplication
from calculator.operations.division import Division
from calculator.history.calculations import Calculations


class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def add_numbers(*args):
        """Adds a list of numbers"""
        addition = Addition(args)
        Calculations.add_calculation(addition)
        return addition.get_result()

    @staticmethod
    def subtract_numbers(*args):
        """Subtracts a list of numbers"""
        subtraction = Subtraction(args)
        Calculations.add_calculation(subtraction)
        return subtraction.get_result()

    @staticmethod
    def multiply_numbers(*args):
        """Multiply a list of numbers"""
        multiplication = Multiplication(args)
        Calculations.add_calculation(multiplication)
        return multiplication.get_result()

    @staticmethod
    def divide_numbers(*args):
        """Divide a list of numbers"""
        division = Division(args)
        Calculations.add_calculation(division)
        return division.get_result()
