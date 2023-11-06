#bryan start working from here 
from flask import Flask, render_template









@app.before_first_request
def import data():
    if Book.query.first() is None: # this only imports if table is empty
        data = pd.read_csv('data.csv')
        for row in data.itertuples():
            db.session.add(Book(title=row.title, author=row.author, year=row.year))
            db.session.commit()

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
