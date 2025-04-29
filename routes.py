from flask import Blueprint, render_template, request
from flask_sqlalchemy import SQLAlchemy

main = Blueprint('main', __name__)
db = SQLAlchemy()

@main.route('/')
def index():
    result = db.session.execute('SELECT name FROM sqlite_master WHERE type="table";')
    tables = [row[0] for row in result]
    return render_template('index.html', tables=tables)
