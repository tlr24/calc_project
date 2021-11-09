"""Multiplication Class"""
from calculator.operations.calculation import Calculation


class Multiplication(Calculation):  # pylint: disable=too-few-public-methods
    """Class for multiplication methods"""
    def get_result(self):
        """Get result of multiplication"""
        product = 1
        for value in self.values:
            product *= value
        return product
