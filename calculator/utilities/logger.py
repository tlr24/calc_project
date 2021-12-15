"""Utility script for logging csv operation results"""
from datetime import datetime
#import pytest
#import calculator.utilities.file_name as fn
from calculator.utilities.file_writer import FileWriter
#from calculator.utilities.csv_reader import CsvReader
#from calculator.utilities.exception_logger import ExceptionLogger
from calculator.calculator import Calculator

class Logger: # pylint: disable=unused-variable,line-too-long,pointless-string-statement
    """Class for parsing and logging results"""

    @staticmethod
    def parse_calculation_to_dict(value1, value2):  # pylint: disable=unused-variable,line-too-long
        """Parsing a calculation from the calculator into a dictionary before performing the operation"""
        output_dict = {'value1': [], 'value2': [], 'result': [], 'operation': [], 'time': []}
        nums = (value1, value2)
        output_dict['value1'].append(value1)
        output_dict['value2'].append(value2)
        output_dict['result'].append(nums)
        output_dict['time'].append(str(datetime.utcnow().timestamp()))
        return output_dict

    @staticmethod
    def log_addition(value1, value2, write_path: str):  # pylint: disable=unused-variable
        """Parsing a calculation from the calculator and adding the values"""
        data_dict = Logger.parse_calculation_to_dict(value1, value2)
        for i in range(len(data_dict['result'])):
            Calculator.addition(data_dict['result'][i])
            data_dict['result'][i] = Calculator.get_last_result_value()
            data_dict['operation'].append("addition")
        FileWriter.append_csv(write_path, data_dict)

    @staticmethod
    def log_subtraction(value1, value2, write_path: str):  # pylint: disable=unused-variable
        """Parsing a calculation from the calculator and subtracting the values"""
        data_dict = Logger.parse_calculation_to_dict(value1, value2)
        for i in range(len(data_dict['result'])):
            Calculator.subtraction(data_dict['result'][i])
            data_dict['result'][i] = Calculator.get_last_result_value()
            data_dict['operation'].append("subtraction")
        FileWriter.append_csv(write_path, data_dict)

    @staticmethod
    def log_multiplication(value1, value2, write_path: str):  # pylint: disable=unused-variable
        """Parsing a calculation from the calculator and multiplying the values"""
        data_dict = Logger.parse_calculation_to_dict(value1, value2)
        for i in range(len(data_dict['result'])):
            Calculator.multiplication(data_dict['result'][i])
            data_dict['result'][i] = Calculator.get_last_result_value()
            data_dict['operation'].append("multiplication")
        FileWriter.append_csv(write_path, data_dict)

    @staticmethod
    def log_division(value1, value2, write_path: str):  # pylint: disable=unused-variable
        """Parsing a calculation from the calculator and dividing the values"""
        data_dict = Logger.parse_calculation_to_dict(value1, value2)
        print(len(data_dict['result']))
        for i in range(len(data_dict['result'])):
            print(data_dict['result'][i])
            '''
            for n in range(len(data_dict['result'][i])):
                if n != 0 and data_dict['result'][i][n] == 0:
                    ExceptionLogger.write_to_exceptions(read_path,i)
                    break
                    # send record number (i) and file name to exemptions log file
            '''
            Calculator.division(data_dict['result'][i])
            data_dict['result'][i] = Calculator.get_last_result_value()
            data_dict['operation'].append("division")
        FileWriter.append_csv(write_path, data_dict)
