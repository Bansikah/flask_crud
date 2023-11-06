
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    year = db.Column(db.Integer)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        new_book = Book(title=request.form['title'], author=request.form['author'], year=request.form['year'])
        db.session.add(new_book)
        db.session.commit()
        return redirect('/')
    return render_template('add_book.html')

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

if __name__ == 'main':
    app.run(host='0.0.0.0', port=8080)
