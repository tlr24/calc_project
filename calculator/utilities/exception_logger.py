"""Utility script for logging csv exemptions"""
import calculator.utilities.file_name as fn
from calculator.utilities.file_writer import FileWriter

class ExceptionLogger: # pylint: disable=too-few-public-methods
    """Class for logging exceptions from csv files to exceptions.csv"""

    @staticmethod
    def write_to_exceptions(file_path: str, record_number):
        """Write exemptions with file name & record number to exemptions.csv"""
        output_string = str(record_number) + "," + fn.get_file_name(file_path)
        FileWriter.append_file('tests/logs/exceptions.csv', output_string)
