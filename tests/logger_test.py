"""Script to test logger functionality"""
import pytest
import calculator.utilities.absolute_path as ap
from calculator.utilities.logger import Logger
from calculator.utilities.file_writer import FileWriter
# pylint: disable=consider-using-with,pointless-string-statement,line-too-long,consider-using-enumerate

@pytest.fixture
def test_csv_fixture(): # pylint: disable=redefined-outer-name,unused-argument,consider-using-with,line-too-long
    """A fixture that will run each time you pass it to a test to generate a test csv history file to read from"""
    path = 'tests/test_data/test_logger.csv'
    test_data = "value1,value2,result,operation,time\n"
    FileWriter.write_to_file(path, test_data)

def test_parse_calculation_to_dict(): # pylint: disable=redefined-outer-name,unused-argument
    """Testing parsing each row of a data frame into a dictionary"""
    # Arrange
    value1 = 1
    value2 = 2
    # Act
    data_dict = Logger.parse_calculation_to_dict(value1, value2)
    # Assert
    assert data_dict['result'] == [(value1, value2)]
    assert data_dict['value1'] == [value1]
    assert data_dict['value2'] == [value2]

def test_log_addition(test_csv_fixture): # pylint: disable=redefined-outer-name,unused-argument
    """Testing parsing each row of a data frame"""
    # Arrange
    value1 = 1
    value2 = 2
    write_path = 'tests/test_data/test_logger.csv'
    # Act
    Logger.log_addition(value1, value2, write_path)
    # Assert
    with open(ap.absolute_path(write_path), 'r', encoding='utf-8') as file:
        test_file = file.readlines()
        assert test_file[-1].replace('\n', '').startswith("1,2,3.0,addition,")

def test_log_subtraction(test_csv_fixture): # pylint: disable=redefined-outer-name,unused-argument
    """Testing parsing each row of a data frame"""
    # Arrange
    value1 = 4
    value2 = 2
    write_path = 'tests/test_data/test_logger.csv'
    # Act
    Logger.log_subtraction(value1, value2, write_path)
    # Assert
    with open(ap.absolute_path(write_path), 'r', encoding='utf-8') as file:
        test_file = file.readlines()
        assert test_file[-1].replace('\n', '').startswith("4,2,2.0,subtraction,")

def test_log_multiplication(test_csv_fixture): # pylint: disable=redefined-outer-name,unused-argument
    """Testing parsing each row of a data frame"""
    # Arrange
    value1 = 5
    value2 = 2
    write_path = 'tests/test_data/test_logger.csv'
    # Act
    Logger.log_multiplication(value1, value2, write_path)
    # Assert
    with open(ap.absolute_path(write_path), 'r', encoding='utf-8') as file:
        test_file = file.readlines()
        assert test_file[-1].replace('\n', '').startswith("5,2,10.0,multiplication,")

def test_log_division(test_csv_fixture): # pylint: disable=redefined-outer-name,unused-argument
    """Testing parsing each row of a data frame"""
    # Arrange
    value1 = 1
    value2 = 2
    write_path = 'tests/test_data/test_logger.csv'
    # Act
    Logger.log_division(value1, value2, write_path)
    # Assert
    with open(ap.absolute_path(write_path), 'r', encoding='utf-8') as file:
        test_file = file.readlines()
        assert test_file[-1].replace('\n', '').startswith("1,2,0.5,division,")
