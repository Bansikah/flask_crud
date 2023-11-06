from flask import Flask



@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
	app.run(port=8080, debug=True)