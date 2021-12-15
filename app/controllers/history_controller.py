"""History controller"""
from flask import render_template, flash
from app.controllers.controller import ControllerBase
from calculator.utilities.csv_reader import CsvReader
from calculator.utilities.file_writer import FileWriter
# pylint: disable=too-few-public-methods,line-too-long

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

    @staticmethod
    def get_clear_data():
        """Method to clear history.csv and return to basic_table.html"""
        FileWriter.write_csv('calculator/results/history.csv', {'value1': [], 'value2': [],'result': [], 'operation': [], 'time': []})
        flash("Calculation history cleared")
        return render_template('basic_table.html')
