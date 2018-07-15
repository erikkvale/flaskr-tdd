import sqlite3
from flask import (
    Flask, request, session, g, redirect,
    url_for, abort, render_template, flash,
    jsonify,
)

# Config
DATABASE = 'flaskr.db'
DEBUG = True
SECRET_KEY = 'my_real_precious'
USERNAME = 'admin'
PASSWORD = 'password'

# Create and initialize app
app = Flask(__name__)
app.config.from_object(__name__)


def init_db():
    """
    Create the database
    """
    with app.app_context():
        db = _open_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def _connect_db():
    """
    Connects to the database
    """
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def _open_db():
    """
    Open database connnection
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = _connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def _close_db(error):
    """
    Close database connection
    """
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


if __name__=='__main__':
    init_db()
    app.run()