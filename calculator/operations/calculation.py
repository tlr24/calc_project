""""Calculation Class"""


class Calculation:
    """Calculation abstract base class"""
    # pylint: disable=too-few-public-methods
    def __init__(self, values: tuple):
        """Constructor method"""
        self.values = Calculation.convert_args_to_list_float(values)

    @classmethod
    def create(cls, values: tuple):
        """Factory method"""
        return cls(values)

    @staticmethod
    def convert_args_to_list_float(values):
        """Standardize values to list of floats"""
        list_values_float = []
        for item in values:
            list_values_float.append(float(item))
        return list_values_float
