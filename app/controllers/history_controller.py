"""History controller"""
from flask import render_template
from app.controllers.controller import ControllerBase
from calculator.utilities.csv_reader import CsvReader
# pylint: disable=too-few-public-methods

class HistoryController(ControllerBase):
    """History controller class"""

    @staticmethod
    def get():
        """Gets data from test addition log and returns to basic_table.html"""
        data_dict = CsvReader.read_csv_dict('tests/logs/test_addition_log.csv')
        return render_template('basic_table.html', data=data_dict)
