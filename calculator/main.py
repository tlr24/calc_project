""" This is the main program """
from calculator.utilities.logger import Logger

Logger.log_addition('../tests/test_data/test_add_data.csv', '../tests/logs/log_addition.csv')
Logger.log_subtraction('../tests/test_data/test_subtract_data.csv', '../tests/logs/log_subtraction.csv')
Logger.log_multiplication('../tests/test_data/test_multiply_data.csv', '../tests/logs/log_multiplication.csv')
Logger.log_division('../tests/test_data/test_divide_data.csv', '../tests/logs/log_division.csv')
print("running")