# Name: Ruben Sanduleac
# Date: March 20th, 2022
# Description: This is a personal blog built using Flask, BootStrap, HTML, CSS, JS, and Python.
import requests
from flask import Flask, render_template

app = Flask(__name__)
url_blog = 'https://api.npoint.io/16660bc83ea958e4eea4'
posts = requests.get(url_blog).json()

@app.route('/')
@app.route('/home')
def index_page():
    return render_template('index.html', all_posts=posts)


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


@app.route('/post/<int:index>')
def post_page(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
            # print(requested_post)
    return render_template('post.html', post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)
