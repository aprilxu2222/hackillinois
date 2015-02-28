from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
    
app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
def welcome():
    return render_template('index.html')

@app.route('/plan')
def plan():
    return render_template('plan.html')

from app import views