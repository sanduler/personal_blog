# Name: Ruben Sanduleac
# Date: March 20th, 2022
# Description: This is a personal blog built using Flask, BootStrap, HTML, CSS, JS, and Python.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
