# save this as app.py
from flask import Flask, url_for, request, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html',
                           para="Sample content",
                           header="Home Page", title="Home")


@app.route('/user/<username>')
def user(username):
    return f'User {escape(username)}'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('user', username='John Doe'))
    url_for('static', filename='style.css')
