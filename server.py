from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/', methods=["GET"])
def main():
    return render_template('main.html')


@app.route('/submit_info', methods=["POST"])
def submit_info():
    title = request.form['title']
    authors = request.form['authors']
    journal = request.form['journal']
    doi = request.form['doi']
    year = request.form['year']
    
    try:
        year = int(year)
        if year < 1000 or year > 9999:
            return "Invalid year", 400
    except ValueError:
        return "Year must be a number", 400
    
    return 'Info submitted successfullly !'


@app.route('/saved_matrix', methods=["GET"])
def saved_matrix():
    return render_template('saved_matrix.html')


@app.route('/about', methods=["GET"])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)