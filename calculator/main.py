""" This is the main calculator program """
from calculator.operations.addition import Addition
from calculator.operations.subtraction import Subtraction
from calculator.operations.multiplication import Multiplication
from calculator.operations.division import Division


class Calculator:
    """ This is the Calculator class"""
    history = []

    @staticmethod
    def clear_history():
        """Clear history of calculations"""
        Calculator.history.clear()

    @staticmethod
    def get_calculation(num):
        """Get a calculation from the history"""
        return Calculator.history[num]

    @staticmethod
    def get_calculation_last():
        """Get the last calculation in history"""
        return Calculator.history[-1]

    @staticmethod
    def add_numbers(*args):
        """Adds a list of numbers"""
        addition = Addition(args)
        Calculator.history.append(addition)
        return addition.get_result()

    @staticmethod
    def subtract_numbers(*args):
        """Subtracts a list of numbers"""
        subtraction = Subtraction(args)
        Calculator.history.append(subtraction)
        return subtraction.get_result()

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """multiply number with result"""
        return Multiplication.multiply(value_a, value_b)

    @staticmethod
    def divide_numbers(value_a, value_b):
        """Divide two numbers"""
        return Division.divide(value_a, value_b)
