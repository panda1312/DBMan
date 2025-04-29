from flask import Blueprint, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

main = Blueprint('main', __name__)
db = SQLAlchemy()

@main.route('/', methods=['GET', 'POST'])
def index():
    tables = []
    query_result = None
    error = None

    if request.method == 'POST':
        sql_query = request.form.get('query')
        try:
            result = db.session.execute(sql_query)
            query_result = result.fetchall()
            db.session.commit()
        except SQLAlchemyError as e:
            error = str(e.__dict__.get('orig'))
            db.session.rollback()
    
    try:
        result = db.session.execute('SELECT name FROM sqlite_master WHERE type="table";')
        tables = [row[0] for row in result]
    except Exception as e:
        error = str(e)

    return render_template('index.html', tables=tables, query_result=query_result, error=error)
