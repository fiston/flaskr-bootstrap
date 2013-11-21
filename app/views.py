from app import app
from app import connect_db

from flask import g
from flask import abort
from flask import flash
from flask import url_for
from flask import session
from flask import request
from flask import redirect
from flask import render_template

GET = 'GET'
POST = 'POST'

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    # app.logger.warning(exception)
    db = getattr(g, 'db', None)
    if db:
        db.close()

@app.after_request
def after_request(obj):
    return obj

@app.route('/')
def index():
    cursor = g.db.execute("select title, text from entries order by id desc")
    posts = [dict(title=row[0], text=row[1]) for row in cursor.fetchall()]
    return render_template('index.html', posts=posts)

@app.route('/add', methods=[POST])
def add():
    if not session.get('logged_in', None):
        abort(401)
    g.db.execute("insert into entries (title, text) values (?, ?)", [request.form['title'], request.form['text']])
    g.db.commit()
    flash("New post submitted!")
    return redirect(url_for('index'))

@app.route('/login', methods=[GET, POST])
def login():
    errors = []
    if request.method == POST:
        if request.form.get('username') != app.config['USERNAME']:
            errors.append('Invalid username')
        elif request.form.get('password') != app.config['PASSWORD']:
            errors.append('Invalid password')
        else:
            session['logged_in'] = True
            flash('Login successful!')
            return redirect(url_for('index'))

    return render_template('login.html', errors=errors)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Logout!')
    return redirect(url_for('index'))
























