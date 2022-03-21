# Name: Ruben Sanduleac
# Date: March 20th, 2022
# Description: This is a personal blog built using Flask, BootStrap, HTML, CSS, JS, and Python.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index_page():
    return render_template('index.html')


@app.route('/about.html')
def about_page():
    return render_template('about.html')


@app.route('/contact.html')
def contact_page():
    return render_template('contact.html')

@app.route('/post.html')
def post_page():
    return render_template('post.html')

if __name__ == '__main__':
    app.run(debug=True)
