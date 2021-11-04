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
        return True

    @staticmethod
    def get_calculation(num):
        """Get a calculation from the history"""
        return Calculator.history[num]

    @staticmethod
    def get_calculation_last():
        """Get the last calculation in history"""
        return Calculator.history[-1]

    @staticmethod
    def count_calculations():
        """Count the number of calculations in history"""
        return len(Calculator.history)

    @staticmethod
    def remove_calculation(num):
        """Remove a specific calculation"""
        Calculator.history.remove(Calculator.history[num])
        return True

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
    def multiply_numbers(*args):
        """Multiply a list of numbers"""
        multiplication = Multiplication(args)
        Calculator.history.append(multiplication)
        return multiplication.get_result()

    @staticmethod
    def divide_numbers(*args):
        """Divide a list of numbers"""
        division = Division(args)
        Calculator.history.append(division)
        return division.get_result()
