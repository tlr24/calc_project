"""A simple flask web app"""
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from werkzeug.debug import DebuggedApplication
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.history_controller import HistoryController
from app.controllers.article_controller import ArticleController
# pylint: disable=line-too-long, no-else-return

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer, index=True)
    address = db.Column(db.String(256))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120), index=True)

db.create_all()


@app.route('/')
def index():
    users = User.query
    return render_template('basic_table.html', title='Basic Table',
                           users=users)
'''

if __name__ == '__main__':
    app.run()

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

@app.route("/api/data", methods=['GET'])
def history_data_get():
    """Get the history table data from the History Controller"""
    return HistoryController.get_data()

@app.route("/aaa_testing", methods=['GET'])
def aaa_testing_get():
    """Get the AAA testing article from the Article Controller"""
    return ArticleController.get_aaa_testing()

@app.route("/oop_glossary", methods=['GET'])
def oop_glossary_get():
    """Get the OOP glossary article from the Article Controller"""
    return ArticleController.get_oop_glossary()

@app.route("/oop_principles", methods=['GET'])
def oop_principles_get():
    """Get the OOP principles article from the Article Controller"""
    return ArticleController.get_oop_principles()

@app.route("/soc", methods=['GET'])
def soc_get():
    """Get the SoC article from the Article Controller"""
    return ArticleController.get_soc()
