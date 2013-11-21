import sqlite3

from flask import Flask
from flask import request
from flask import session
from flask import g
from flask import redirect
from flask import url_for
from flask import abort
from flask import render_template
from flask import flash

from contextlib import closing

from config import *

app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    # app.logger.debug(app.config['DATABASE'])
    return sqlite3.connect(app.config['DATABASE'])


from app import views




