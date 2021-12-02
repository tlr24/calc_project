""" This is the main program """
from calculator.utilities.csv_reader import CsvReader
# from calculator.utilities.file_writer import FileWriter

def read_csv(path: str):
    """Read csv files"""
    csv = CsvReader.read_csv(path)
    print(csv.to_string())
    # for i in range(len)

test_dict = CsvReader.read_csv_dict('../tests/test_data/test_add_data.csv')
CsvReader.parse_addition_df(test_dict)
print("running")
# read_csv('../tests/test_data/test_add_data.csv')
# read_csv('../tests/test_data/test_subtract_data.csv')
# read_csv('../tests/test_data/test_multiply_data.csv')
# read_csv('../tests/test_data/test_divide_data.csv')
