import os
from flask import Flask, render_template, request, redirect, url_for
from src.common.database import Database
from src.models.post import Post


app = Flask(__name__)
app.config.from_object('src.config')
app.secret_key = os.environ.get('APP_SECRET_KEY')


@app.before_first_request
def init_db():
    Database.initialize()
    Database.purge()


@app.route('/')
def index():
    posts = Post.all()
    return render_template('index.html', posts=posts)


@app.route('/add_post', methods=['POST'])
def add_post():
    title = request.form['title']
    author = request.form['author']
    content = request.form['content']

    blog_post = Post(title=title, author=author, content=content)
    blog_post.save_to_mongo()

    return redirect(url_for('index'))


@app.route('/add')
def add():
    return render_template('add.html')
