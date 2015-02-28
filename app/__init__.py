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

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

from app import views