##https://pythonhow.com/building-a-website-with-python-flask/ This website is created with reference too
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home1.html')


@app.route('/about/')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)

