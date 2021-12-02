"""Utility script for logging csv operation results"""
from datetime import datetime
#import pytest
import calculator.utilities.file_name as fn
from calculator.utilities.file_writer import FileWriter
from calculator.utilities.csv_reader import CsvReader
#from calculator.utilities.exception_logger import ExceptionLogger
from calculator.calculator import Calculator

class Logger: # pylint: disable=unused-variable,line-too-long,pointless-string-statement
    """Class for parsing and logging results from csv files"""

    @staticmethod
    def parse_df_to_dict(read_path: str):  # pylint: disable=unused-variable,line-too-long
        """Parsing a data frame derived from a csv into a dictionary before performing the operation"""
        data_frame = CsvReader.read_csv(read_path)
        output_dict = {'result': [], 'time': [], 'filename': [], 'recordNumber': [], 'operation': []}
        for index, row in data_frame.iterrows():
            value1 = row['value_1']
            value2 = row['value_2']
            nums = (value1, value2)
            output_dict['result'].append(nums)
            output_dict['time'].append(str(datetime.utcnow().timestamp()))
            output_dict['filename'].append(fn.get_file_name(read_path))
            output_dict['recordNumber'].append(index+1)
        return output_dict

    @staticmethod
    def log_addition(read_path: str, write_path: str):  # pylint: disable=unused-variable
        """Parsing a data frame derived from a csv and adding all of the values per row"""
        data_dict = Logger.parse_df_to_dict(read_path)
        for i in range(len(data_dict['result'])):
            Calculator.add_numbers(data_dict['result'][i])
            data_dict['result'][i] = Calculator.get_last_result_value()
            data_dict['operation'].append("addition")
        FileWriter.write_csv(write_path, data_dict)

    @staticmethod
    def log_subtraction(read_path: str, write_path: str):  # pylint: disable=unused-variable
        """Parsing a data frame derived from a csv and subtracting all of the values per row"""
        data_dict = Logger.parse_df_to_dict(read_path)
        for i in range(len(data_dict['result'])):
            Calculator.subtract_numbers(data_dict['result'][i])
            data_dict['result'][i] = Calculator.get_last_result_value()
            data_dict['operation'].append("subtraction")
        FileWriter.write_csv(write_path, data_dict)

    @staticmethod
    def log_multiplication(read_path: str, write_path: str):  # pylint: disable=unused-variable
        """Parsing a data frame derived from a csv and multiplying all of the values per row"""
        data_dict = Logger.parse_df_to_dict(read_path)
        for i in range(len(data_dict['result'])):
            Calculator.multiply_numbers(data_dict['result'][i])
            data_dict['result'][i] = Calculator.get_last_result_value()
            data_dict['operation'].append("multiplication")
        FileWriter.write_csv(write_path, data_dict)

    @staticmethod
    def log_division(read_path: str, write_path: str):  # pylint: disable=unused-variable
        """Parsing a data frame derived from a csv and dividing all of the values per row"""
        data_dict = Logger.parse_df_to_dict(read_path)
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
            Calculator.divide_numbers(data_dict['result'][i])
            data_dict['result'][i] = Calculator.get_last_result_value()
            data_dict['operation'].append("division")
        FileWriter.write_csv(write_path, data_dict)
