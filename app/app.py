import flask
from flask import Flask, render_template, redirect, session, request
import sqlite3


app = Flask(__name__)

# Getting configuration variables from config.py
app.config.from_pyfile('config.py')

app.secret_key = app.config['SECRET_KEY']
Db = app.config['DB']


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/login", methods=['GET','POST'])
def login():
    global Db
    if flask.request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        query = "SELECT * FROM users where username='%s' and password='%s';" % (username, password)
        results = Db.exec_query(query)
        if len(results) == 0:
            return render_template('login.html')
        #' or 1=1 --
        print(query, results)
        return render_template('profile.html', user=results[0])
    else:
        return render_template('login.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if flask.request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        query = "insert into users values('%s','%s','user');" %(username,password)
        results = Db.exec_query(query)
        if len(results) == 0:
            return render_template('register.html')
        return render_template('profile.html', user=results[0])
    else:
        return render_template('register.html')


