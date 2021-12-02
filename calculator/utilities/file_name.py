"""Script that holds get file name utility function"""
import os
import calculator.utilities.absolute_path as ap


def get_file_name(filepath: str):
    """Method to get file name from a path"""
    file_name = os.path.basename(ap.absolute_path(filepath))
    return file_name
