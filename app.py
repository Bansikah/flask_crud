from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    year = db.Column(db.Integer)

data_imported = False

@app.before_request
def import_data():
    global data_imported
    if not data_imported:
        db.create_all()
        if Book.query.first() is None:  # Only import if table is empty
            data = pd.read_csv('data.csv')
            for _, row in data.iterrows():
                db.session.add(Book(title=row['title'],author=row['author'],year=row['year']))
            db.session.commit()
        data_imported = True

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)




