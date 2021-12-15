"""Script to test exception logger functionality"""
import calculator.utilities.absolute_path as ap
from calculator.utilities.exception_logger import ExceptionLogger
from calculator.utilities.file_writer import FileWriter
#from calculator.utilities.csv_reader import CsvReader

def test_write_to_exceptions():
    """Testing writing exemptions with file name & record number to exemptions.csv"""
    # Arrange
    value1 = 1
    value2 = 0
    file_path = 'tests/logs/test_exceptions.csv'
    FileWriter.write_csv(file_path, {'value1': [], 'value2': [], 'operation': [], 'time': []})
    # Act
    ExceptionLogger.write_to_exceptions(value1, value2, file_path)
    # Assert
    with open(ap.absolute_path(file_path), 'r', encoding='utf-8') as file:
        test_file = file.readlines()
        assert test_file[-1].replace('\n', '').startswith("1,0,division,")
    # assert CsvReader.read_csv_dict(file_path) == ''
