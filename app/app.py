"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.history_controller import HistoryController
# pylint: disable=line-too-long, no-else-return

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    """Get the index page from the Index Controller"""
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    """Get the calculator page from the Calculator Controller"""
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    """Post to the Calculator page with the Calculator Controller"""
    return CalculatorController.post()

@app.route("/history", methods=['GET'])
def history_get():
    """Get the history table page from the History Controller"""
    return HistoryController.get()
