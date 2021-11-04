"""Addition Class"""
from calculator.operations.calculation import Calculation


class Addition(Calculation):  # pylint: disable=too-few-public-methods
    """Class for addition methods"""
    def get_result(self):
        """Get result of addition"""
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values = value + sum_of_values
        return sum_of_values
