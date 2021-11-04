"""Division Class"""
from calculator.operations.calculation import Calculation


class Division(Calculation):  # pylint: disable=too-few-public-methods
    """Class for division methods"""
    def get_result(self):
        """Get result of division"""
        try:
            quotient = self.values[0]
            for value in self.values[1:]:
                quotient /= value
            return quotient
        except ZeroDivisionError:
            return None
