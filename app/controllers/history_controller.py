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
        data_dict = CsvReader.read_csv_dict('calculator/results/history.csv')
        return render_template('basic_table.html', data=data_dict)

    @staticmethod
    def get_data():
        """Method to get data for ajax"""
        data_dict = CsvReader.read_csv_dict('calculator/results/history.csv')
        return {'data': data_dict}
