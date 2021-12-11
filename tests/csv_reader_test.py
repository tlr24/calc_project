"""Script to test pandas functionality"""
import pandas as pd
import pytest
from calculator.utilities.csv_reader import CsvReader
from calculator.utilities.file_writer import FileWriter
# pylint: disable=line-too-long

@pytest.fixture
def add_test_csv_fixture(): # pylint: disable=redefined-outer-name,unused-argument,consider-using-with
    """A fixture that will run each time you pass it to a test to read csv files"""
    path = 'tests/test_data/test_csv_reader.csv'
    test_data = "value_1,value_2,total\n1,2,3\n2,3,5"
    FileWriter.write_to_file(path, test_data)

def test_read_csv(add_test_csv_fixture): # pylint: disable=redefined-outer-name,unused-argument
    """Testing reading csv files as data frames"""
    # Arrange
    path = 'tests/test_data/test_csv_reader.csv'
    # Act
    data = CsvReader.read_csv(path)
    # Assert
    assert isinstance(data, pd.DataFrame)

def test_read_csv_dict(add_test_csv_fixture): # pylint: disable=redefined-outer-name,unused-argument
    """Testing reading csv files as a dictionary"""
    # Arrange
    path = 'tests/test_data/test_csv_reader.csv'
    # Act
    data = CsvReader.read_csv_dict(path)
    # Assert
    assert data == [{'value_1': 1, 'value_2': 2, 'total': 3}, {'value_1': 2, 'value_2': 3, 'total': 5}]
