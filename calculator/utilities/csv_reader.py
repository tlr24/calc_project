"""Utility script for pandas csv_reader"""
import pandas as pd
import calculator.utilities.absolute_path as ap

class CsvReader: # pylint: disable=pointless-string-statement,consider-using-enumerate,line-too-long,unused-variable,too-few-public-methods
    """Class for reading csv's"""

    @staticmethod
    def read_csv(path: str):
        """Read the csv and return its data frame"""
        csv = pd.read_csv(ap.absolute_path(path))
        data_frame = pd.DataFrame(csv)
        return data_frame
