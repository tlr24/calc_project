"""Script to test exception logger functionality"""
#import pandas as pd
from calculator.utilities.exception_logger import ExceptionLogger
from calculator.utilities.file_writer import FileWriter
#from calculator.utilities.csv_reader import CsvReader

def test_write_to_exceptions():
    """Testing writing exemptions with file name & record number to exemptions.csv"""
    # Arrange
    file_path = 'tests/logs/test_exceptions.csv'
    record_number = 1
    FileWriter.write_to_file(file_path, "")
    # Act
    ExceptionLogger.write_to_exceptions(file_path, record_number)
    # Assert
    # assert CsvReader.read_csv(file_path).to_dict == ''
