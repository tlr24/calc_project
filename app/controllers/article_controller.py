"""Article controller"""
from flask import render_template
from app.controllers.controller import ControllerBase
# pylint: disable=too-few-public-methods

class ArticleController(ControllerBase):
    """Article controller class"""

    @staticmethod
    def get_aaa_testing():
        """Returns to AAA_Testing.html"""
        return render_template('AAA_Testing.html')

    @staticmethod
    def get_oop_glossary():
        """Returns to OOPglossary.html"""
        return render_template('OOPglossary.html')

    @staticmethod
    def get_oop_principles():
        """Returns to OOPprinciples.html"""
        return render_template('OOPprinciples.html')

    @staticmethod
    def get_soc():
        """Returns to SOC.html"""
        return render_template('SOC.html')
