"""Script for writing to file utility"""
# import time
import calculator.utilities.absolute_path as ap

class FileWriter: # pylint: disable=too-few-public-methods,consider-using-with
    """Class for writing to files"""

    @staticmethod
    def write_to_file(path: str, file_content: str):
        """Write a string's content to a designated file path"""
        with open(ap.absolute_path(path), "w", encoding='utf-8') as file:
            file.write(file_content)
            file.close()
