"""Division Class"""
from calculator.operations.calculation import Calculation


class Division(Calculation):  # pylint: disable=too-few-public-methods
    """Class for division methods"""
    def get_result(self):
        """Get result of division"""
        quotient = self.values[0]
        for value in self.values[1:]:
            quotient /= value
            #if value == 0:
            #    raise ZeroDivisionError("Can't divide by 0")
        return quotient
