#!/usr/bin/python3

import pymysql
import sys

def connection():
    self.db = pymysql.connect("127.0.0.1", "root", "NitrotheGreat22!", "clientDB")

    self.db.autocommit(True)

    self.cur = self.db.cursor()

def main():
    connection()

if __name__ == "__main__":

    main()
