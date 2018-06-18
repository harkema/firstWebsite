#!/usr/bin/env

from flask import Flask, render_template
from connection import connection
import sqlite3

app=Flask(__name__)

@app.route("/")


def foundation():
    return render_template("base.html")

@app.route('/dashboard/', methods=['GET'])
def dashboard():
    cur, cxn =  connection()
    cur.execute("SELECT * FROM CLIENT")
    data=cur.fetchall()

if __name__ == "__main__":
    app.run(debug=True)
