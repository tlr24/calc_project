""" This is the increment function"""
from calculator.operations.addition import Addition
from calculator.operations.subtraction import Subtraction
from calculator.operations.multiplication import Multiplication
from calculator.operations.division import Division


class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def add_numbers(value_a, value_b):
        """ adds number to result"""
        return Addition.add(value_a, value_b)

    @staticmethod
    def subtract_numbers(value_a, value_b):
        """ subtract number from result"""
        return Subtraction.subtract(value_a, value_b)

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """multiply number with result"""
        return Multiplication.multiply(value_a, value_b)

    @staticmethod
    def divide_numbers(value_a, value_b):
        """Divide two numbers"""
        return Division.divide(value_a, value_b)
