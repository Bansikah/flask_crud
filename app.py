from flask import Flask, render_template, request, redirect
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


@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)


@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        new_book = Book(title=request.form['title'], author=request.form['author'], year=request.form['year'])
        db.session.add(new_book)
        db.session.commit()
        return redirect('/')
    return render_template('add_book.html')
    
    
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


@app.route('/delete/<int:id>')# represents a dynamic parameter indicating the ID of the book to be deleted. 
def delete_book(id):
    book_to_delete = Book.query.get_or_404(id)#used to retrieve the book with the specific id if not found returns 404
    db.session.delete(book_to_delete)#removes the book record from the database
    db.session.commit()#saves the changes made in the database delete session
    return redirect('/')  #Redirects to the user template showing that the data has been deleted                      

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)

