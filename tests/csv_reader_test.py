"""Script to test pandas functionality"""
import pandas as pd
import pytest
import calculator.utilities.absolute_path as ap
from calculator.utilities.csv_reader import CsvReader
from calculator.utilities.file_writer import FileWriter
# pylint: disable=consider-using-with,pointless-string-statement,line-too-long,consider-using-enumerate

@pytest.fixture
def add_test_csv_fixture(): # pylint: disable=redefined-outer-name,unused-argument,consider-using-with
    """A fixture that will run each time you pass it to a test to read csv files"""
    path = 'tests/test_data/test_csv_reader.csv'
    test_data = "value_1,value_2,total\n1,2,3\n2,3,5"
    FileWriter.write_to_file(path, test_data)

def test_read_csv(add_test_csv_fixture): # pylint: disable=redefined-outer-name,unused-argument,consider-using-with
    """Testing reading csv files as data frames"""
    # Arrange
    path = 'tests/test_data/test_csv_reader.csv'
    # Act
    data = CsvReader.read_csv(path)
    # Assert
    assert isinstance(data, pd.DataFrame)

def test_read_csv_dict(add_test_csv_fixture): # pylint: disable=redefined-outer-name,unused-argument,line-too-long
    """Testing converting a data frame read from a csv to a dictionary"""
    # Arrange
    path = 'tests/test_data/test_csv_reader.csv'
    data = CsvReader.read_csv(path)
    # Act
    test_dict = CsvReader.read_csv_dict(data)
    # Assert
    assert test_dict == {0: {'total': 3, 'value_1': 1, 'value_2': 2}, 1: {'total': 5, 'value_1': 2, 'value_2': 3}}

def test_parse_addition_dict(add_test_csv_fixture): # pylint: disable=redefined-outer-name,unused-argument,consider-using-enumerate
    """Testing parsing each row of a dictionary converted csv"""
    # Arrange
    path = 'tests/test_data/test_csv_reader.csv'
    data = CsvReader.read_csv(path)
    test_dict = CsvReader.read_csv_dict(data)
    # Act
    CsvReader.parse_addition_dict(test_dict)
    # Assert
    with open(ap.absolute_path('tests/test_data/test.csv'), 'r', encoding='utf-8') as file:
        test_file = file.readlines()
        for i in range(len(test_file)):
            if i != 0: # skip the first line with column labels
                # print(test_file[i])
                # print(test_dict[i-1])
                assert test_file[i].replace('\n', '').split(',')[-1] == str(float(test_dict[i-1]['total']))

"""
def test_to_string(add_test_csv_fixture): # pylint: disable=redefined-outer-name,unused-argument,consider-using-with
    # Testing the csv reading utility function from pandas
    # Arrange
    path = 'tests/test_data/test_csv_reader.csv'
    # Act
    data = CsvReader.read_csv(path)
    # Assert
    assert data.to_string() == "   value_1  value_2  total\n" \
                               "0        1        2      3\n1        2        3      5"
"""
