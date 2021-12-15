"""Controller for the calculator"""
from flask import render_template, request, flash #, redirect, url_for, session
from app.controllers.controller import ControllerBase
from calculator.calculator import Calculator
from calculator.utilities.logger import Logger
# pylint: disable=line-too-long


class CalculatorController(ControllerBase):
    """Class for Calculator Controller"""

    @staticmethod
    def post():
        """Method to post to the calculator"""
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'You must enter a value for value 1 and or value 2'
        else:
            flash('Successful calculation')
            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())
            getattr(Logger, "log_" + operation)(value1, value2, 'calculator/results/history.csv')
            return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result)
        return render_template('calculator2.html', error=error)

    @staticmethod
    def get():
        """Method to get calculator2.html"""
        return render_template('calculator2.html')
