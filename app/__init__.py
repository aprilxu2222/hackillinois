from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
    
app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/addtask')
def addtask():
    return render_template('addtask.html')

@app.route('/today')
def today():
    return render_template('today.html')

from app import views