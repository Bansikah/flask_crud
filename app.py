from flask import Flask, render_template, redirect
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

@app.before_request
def import_data_func():
    db.create_all()
    if Book.query.first() is None:  # Only import if table is empty
        data = pd.read_csv('data.csv')
        for row in data.itertuples():
            db.session.add(Book(title=row.title, author=row.author, year=row.year))
        db.session.commit()

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)


@app.route('/delete/<int:id>')# represents a dynamic parameter indicating the ID of the book to be deleted. 
def delete_book(id):
    book_to_delete = Book.query.get_or_404(id)#used to retrieve the book with the specific id if not found returns 404
    db.session.delete(book_to_delete)#removes the book record from the database
    db.session.commit()#saves the changes made in the database delete session
    return redirect('/')  #Redirects to the user template showing that the data has been deleted                      

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
