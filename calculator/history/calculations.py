""""Calculation history class"""
from calculator.operations.addition import Addition
from calculator.operations.subtraction import Subtraction
from calculator.operations.multiplication import Multiplication
from calculator.operations.division import Division


class Calculations:
    """Calculation history abstract base class"""
    # pylint: disable=too-few-public-methods
    history = []

    @staticmethod
    def add_calculation(calculation):
        """Add a calculation to the history"""
        Calculations.history.append(calculation)
        return True

    @staticmethod
    def clear_history():
        """Clear history of calculations"""
        Calculations.history.clear()
        return True

    @staticmethod
    def get_calculation(num):
        """Get a calculation from the history"""
        return Calculations.history[num]

    @staticmethod
    def count_calculations():
        """Count the number of calculations in history"""
        return len(Calculations.history)

    @staticmethod
    def remove_calculation(num):
        """Remove a specific calculation"""
        Calculations.history.remove(Calculations.history[num])
        return True

    @staticmethod
    def get_calculation_first():
        """Get the first calculation in history"""
        return Calculations.history[0]

    @staticmethod
    def get_calculation_first_result():
        """Get the result of the first calculation in history"""
        return Calculations.history[0].get_result()

    @staticmethod
    def get_calculation_last():
        """Get the last calculation in history"""
        return Calculations.history[-1]

    @staticmethod
    def get_calculation_last_result():
        """Get the result of the last calculation in history"""
        return Calculations.history[-1].get_result()

    @staticmethod
    def add_addition_calculation(values):
        """Create an addition and add object to history using factory method create"""
        Calculations.add_calculation(Addition.create(values))
        # Get the result of the calculation
        return True

    @staticmethod
    def add_subtraction_calculation(values):
        """Create a subtraction object to history using factory method create"""
        Calculations.add_calculation(Subtraction.create(values))
        return True

    @staticmethod
    def add_multiplication_calculation(values):
        """Add a multiplication object to history using factory method create"""
        Calculations.add_calculation(Multiplication.create(values))
        return True

    @staticmethod
    def add_division_calculation(values):
        """Add a division object to history using factory method create"""
        Calculations.add_calculation(Division.create(values))
        return True
