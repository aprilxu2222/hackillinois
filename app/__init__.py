import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

from contextlib import closing

# configuration
DATABASE = 'database.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
    
app = Flask(__name__)
app.config.from_object(__name__)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
        
@app.route("/", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You are logged in')
            return redirect(url_for('today'))
    return render_template('login.html', title='Welcome', error=error)

@app.route("/show_entries")
def show_entries():
    cur = g.db.execute('select name, duration from tasks')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('today.html', entries=entries)

@app.route('/', methods=['GET','POST'])
def addtask():
    #if not session.get('logged_in'):
     #   abort(401)
    g.db.execute('insert into tasks (name, deadline, duration) values (?, ?, ?)', [request.form['name'], request.form['deadline'], request.form['duration']])
    g.db.commit()
    flash('New entry was successfully posted')
    return render_template('addtask.html', title='Add Task')

@app.route('/addtaskhtml')
def addtaskhtml():
    return render_template('addtask.html', title='Add Task')

@app.route('/today')
def today():
    return render_template('today.html', title='Today\'s Tasks')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))

from app import views