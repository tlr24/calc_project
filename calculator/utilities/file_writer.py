"""Script for writing to file utility"""
# import time
import pandas as pd
import calculator.utilities.absolute_path as ap

class FileWriter: # pylint: disable=too-few-public-methods,consider-using-with, pointless-string-statement
    """Class for writing to files"""

    '''
    @staticmethod
    def write_csv(path: str, data_dict: dict):
        """Write to a csv"""
        data_frame = pd.DataFrame(data_dict)
        data_frame.to_csv(ap.absolute_path(path), index=False)
    '''

    @staticmethod
    def append_csv(path: str, data_dict: dict):
        """Write to a csv"""
        data_frame = pd.DataFrame(data_dict)
        data_frame.to_csv(ap.absolute_path(path), mode='a', index=False, header=False)

    @staticmethod
    def write_to_file(path: str, file_content: str):
        """Write a string's content to a designated file path"""
        with open(ap.absolute_path(path), "w", encoding='utf-8') as file:
            file.write(file_content)
            file.close()

    @staticmethod
    def append_file(path: str, file_content: str):
        """Write a string's content to a designated file path"""
        with open(ap.absolute_path(path), "a", encoding='utf-8') as file:
            file.write(file_content)
            file.close()
