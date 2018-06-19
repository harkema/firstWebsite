#!/usr/bin/python3

from dBConnection import connection
import mysql.connector


def main():
    cur, cxn =  connection()
    cur.execute("SELECT * FROM Client")
    data=cur.fetchall()

if __name__ == "__main__":
    main()
