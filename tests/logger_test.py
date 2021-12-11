"""Script to test logger functionality"""
#import pytest
import calculator.utilities.absolute_path as ap
import calculator.utilities.file_name as fn
from calculator.utilities.csv_reader import CsvReader
from calculator.utilities.logger import Logger
# pylint: disable=consider-using-with,pointless-string-statement,line-too-long,consider-using-enumerate

def test_parse_df_to_dict(): # pylint: disable=redefined-outer-name,unused-argument
    """Testing parsing each row of a data frame into a dictionary"""
    # Arrange
    path = 'tests/test_data/test_add_data.csv'
    # Act
    data_dict = Logger.parse_df_to_dict(path)
    # Assert
    for i in range(len(data_dict['result'])):
        assert data_dict['result'][i] == (CsvReader.read_csv(path)['value_1'][i], CsvReader.read_csv(path)['value_2'][i])
        assert data_dict['filename'][i] == fn.get_file_name(path)
        assert data_dict['recordNumber'][i] == i+1

def test_log_addition(): # pylint: disable=redefined-outer-name,unused-argument
    """Testing parsing each row of a data frame"""
    # Arrange
    read_path = 'tests/test_data/test_add_data.csv'
    data = CsvReader.read_csv(read_path)
    # Act
    Logger.log_addition(read_path, 'tests/logs/test_addition_log.csv')
    # Assert
    with open(ap.absolute_path('tests/logs/test_addition_log.csv'), 'r', encoding='utf-8') as file:
        test_file = file.readlines()
        # print(data['total'])
        for i in range(len(test_file)):
            if i != 0:  # skip the first line with column labels
                assert test_file[i].replace('\n', '').split(',')[0] == str(data['total'][i-1].astype(float))

def test_log_subtraction(): # pylint: disable=redefined-outer-name,unused-argument
    """Testing parsing each row of a data frame"""
    # Arrange
    read_path = 'tests/test_data/test_subtract_data.csv'
    data = CsvReader.read_csv(read_path)
    # Act
    Logger.log_subtraction(read_path, 'tests/logs/test_subtraction_log.csv')
    # Assert
    with open(ap.absolute_path('tests/logs/test_subtraction_log.csv'), 'r', encoding='utf-8') as file:
        test_file = file.readlines()
        for i in range(len(test_file)):
            if i != 0:  # skip the first line with column labels
                assert test_file[i].replace('\n', '').split(',')[0] == str(data['total'][i-1].astype(float))

def test_log_multiplication(): # pylint: disable=redefined-outer-name,unused-argument
    """Testing parsing each row of a data frame"""
    # Arrange
    read_path = 'tests/test_data/test_multiply_data.csv'
    data = CsvReader.read_csv(read_path)
    # Act
    Logger.log_multiplication(read_path, 'tests/logs/test_multiplication_log.csv')
    # Assert
    with open(ap.absolute_path('tests/logs/test_multiplication_log.csv'), 'r', encoding='utf-8') as file:
        test_file = file.readlines()
        for i in range(len(test_file)):
            if i != 0:  # skip the first line with column labels
                assert test_file[i].replace('\n', '').split(',')[0] == str(data['total'][i-1].astype(float))

def test_log_division(): # pylint: disable=redefined-outer-name,unused-argument
    """Testing parsing each row of a data frame"""
    # Arrange
    read_path = 'tests/test_data/test_divide_data.csv'
    data = CsvReader.read_csv(read_path)
    # Act
    Logger.log_division(read_path, 'tests/logs/test_division_log.csv')
    # Assert
    with open(ap.absolute_path('tests/logs/test_division_log.csv'), 'r', encoding='utf-8') as file:
        test_file = file.readlines()
        for i in range(len(test_file)):
            if i != 0:  # skip the first line with column labels
                assert round(float(test_file[i].replace('\n', '').split(',')[0]), 9) == data['total'][i-1].astype(float)
