"""Utility script for pandas csv_reader"""
from datetime import datetime
import pandas as pd
import calculator.utilities.absolute_path as ap
from calculator.utilities.file_writer import FileWriter
from calculator.calculator import Calculator

class CsvReader: # pylint: disable=too-few-public-methods,pointless-string-statement,consider-using-enumerate,line-too-long
    """Class for reading csv's"""

    @staticmethod
    def read_csv(path: str):
        """Read the csv and return its data frame"""
        csv = pd.read_csv(ap.absolute_path(path))
        data_frame = pd.DataFrame(csv)
        return data_frame

    @staticmethod
    def read_csv_dict(data_frame: pd.DataFrame):
        """Take in a data frame and return it as a dictionary"""
        return data_frame.to_dict(orient='index')

    @staticmethod
    def parse_addition_dict(addition_dict: dict): # pylint: disable=consider-using-enumerate,line-too-long
        """Go through a dictionary derived from a csv and add all of the values per row"""
        output_string = 'time,result\n'
        for i in range(len(addition_dict)):
            num_list = []
            for j in addition_dict[i].keys():
                print(addition_dict[i][j])
                if j != "total":
                    num_list.append(addition_dict[i][j])
            Calculator.add_numbers(tuple(num_list))
            output_string += str(datetime.utcnow().timestamp()) + ',' + str(Calculator.get_last_result_value()) + '\n'
        FileWriter.write_to_file('tests/test_data/test.csv', output_string)
        return output_string

    """@staticmethod
    def to_string(data_frame: pd.DataFrame):
        # Returns the data frame contents as a string
        return data_frame.to_string()"""
