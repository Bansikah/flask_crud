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

@app.route('/edit_book/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = Book.query.get(book_id)
    
    if request.method == 'POST':
        # Update the book details based on the form data 
        book.title = request.form['title']
        book.author = request.form['author']
        book.year = int(request.form['year'])
        db.session.commit()
        
        return redirect('/')
    
    return render_template('edit_book.html', book=book)

if __name__ == '__main__':
    app.run(port=8080, debug=True)



