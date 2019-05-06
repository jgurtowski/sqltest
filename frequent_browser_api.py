#!/usr/bin/env python

from flask import Flask, jsonify, g
import sqlite3

app = Flask(__name__)

DB_FILE = "testdb.db"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB_FILE)
    return db


@app.route('/frequent_browsers')
def freq_browsers():
    cursor = get_db().cursor()
    data = cursor.execute("select * from frequent_browsers limit 10;")
    headers = list(map(lambda x: x[0], cursor.description))
    dict_data = map(lambda x: dict(zip(headers,x)), data)
    return jsonify(list(dict_data))

    
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if not db is None:
        db.close()


if __name__ == '__main__':
    app.run(debug=True)
        


    
    
