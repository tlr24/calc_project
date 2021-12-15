"""Utility script for logging csv exemptions"""
from datetime import datetime
from calculator.utilities.file_writer import FileWriter

class ExceptionLogger: # pylint: disable=too-few-public-methods
    """Class for logging exceptions from csv files to exceptions.csv"""

    @staticmethod
    def write_to_exceptions(value1, value2, write_path: str):
        """Write exemptions to exemptions.csv"""
        output_dict = {'value1': [], 'value2': [], 'operation': [], 'time': []}
        output_dict['value1'].append(value1)
        output_dict['value2'].append(value2)
        output_dict['time'].append(str(datetime.utcnow().timestamp()))
        output_dict['operation'].append("division")
        FileWriter.append_csv(write_path, output_dict) # 'tests/logs/exceptions.csv'
