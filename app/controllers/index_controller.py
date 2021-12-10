"""Index controller"""
from flask import render_template
from app.controllers.controller import ControllerBase
# pylint: disable=too-few-public-methods

class IndexController(ControllerBase):
    """Index controller class"""

    @staticmethod
    def get():
        """Returns to index.html"""
        return render_template('index.html')
