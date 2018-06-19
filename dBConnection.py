#!/usr/bin/python3

import mysql.connector
import sys

def connection():
    cxn = mysql.connector.connect(user ="root", password = "NitrotheGreat22!", host =  "127.0.0.1", database= "clientDB")

    cur = cxn.cursor()

    cur.execute("SELECT * FROM Client")

    results=cur.fetchall()

    print("type", type(results))

    return cxn, cur

def main():
    connection()

if __name__ == "__main__":

    main()
