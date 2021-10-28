"""Division Class"""


class Division:  # pylint: disable=too-few-public-methods
    """Class for division methods"""

    @staticmethod
    def divide(value_a, value_b):
        """Dividing two values"""
        try:
            return value_a / value_b
        except ZeroDivisionError:
            return None
