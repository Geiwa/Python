from flask import Flask
from markupsafe import escape 
from flask  import url_for
from flask import request 
from flask import render_template
app = Flask(__name__)

# @app.route("/<name>")

# def message(name):
#     return f"<h1> Hello {escape(name)} !"

@app.route("/index")
@app.route("/index/<name>")
def index(name=None):
    return render_template("index.html",name=name)

@app.route("/about")
def about():
    return "Это  страницв о нашей компании"

@app.route("/user/<username>")
def show_user_profile(username):
    return f"Это пользователь {escape(username)}"



@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route("/login")
def login():
    return "Страничка входа"

@app.route("/user/<username>")
def profile(username):
    return f"{username}\'s profile"


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Alia'))



