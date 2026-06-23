#!/usr/bin/python3
import MySQLdb
import sys
"""query data"""


if __name__ == "__main__":
    argv_params = sys.argv
    if len(argv_params) < 4:
        raise ValueError("Not enough system parameter provided")
    db = MySQLdb.connect(host='localhost', user=argv_params[1], passwd=argv_params[2], db=argv_params[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print (row)