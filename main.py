# Name: Ruben Sanduleac
# Date: March 20th, 2022
# Description: This is a personal blog built using Flask, BootStrap, HTML, CSS, JS, and Python.
import requests
from flask import Flask, render_template

app = Flask(__name__)
url_blog = 'https://api.npoint.io/16660bc83ea958e4eea4'
posts = requests.get(url_blog).json()

@app.route('/')
@app.route('/index.html')
def index_page():
    return render_template('index.html', all_posts=posts)


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
