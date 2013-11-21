import os
import sqlite3
from config import DATABASE
from contextlib import closing


def init_db(schema='app/schema.sql'):    
    print 'DATABASE', DATABASE
    root = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(root, schema)
    with closing(sqlite3.connect(DATABASE)) as db:
        with open(filepath, 'r') as f:
            db.cursor().executescript(f.read())
        db.commit()


if __name__ == '__main__':
    init_db()