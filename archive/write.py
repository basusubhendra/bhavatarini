#!/usr/bin/python3
import sys
import mariadb

db = mariadb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="zeros")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()
f = open("zeros6","r")
lines = f.readlines()
for l in lines:
    line = str(l).lstrip().rstrip()
    idx = line.index(".")
    line = line[:idx]
    cur.execute("INSERT INTO zeros (value) values (" + str(line) + ")")
    db.commit()
db.close()
