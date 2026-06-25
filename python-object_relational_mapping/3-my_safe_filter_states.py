#!/usr/bin/python3
"""Module for ORM to list all states - safe from SQL injection"""

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = conn.cursor()

    cur.execute("SELECT * FROM states "
                "WHERE name = BINARY %s "
                "ORDER BY states.id ASC", (sys.argv[4],))

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
