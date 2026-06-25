#!/usr/bin/python3
"""Module for ORM to list all states from hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = conn.cursor()

    search_name = sys.argv[4]
    cur.execute("SELECT * FROM states "
                "WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(search_name))
    query_rows = cur.fetchall()
    # print(query_rows)
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
