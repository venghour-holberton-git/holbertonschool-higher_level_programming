#!/usr/bin/python3
"""A script that lists all states matching the provided name"""

import sys
import MySQLdb

# Connect to the MySQL server using credentials and db name
# passed in as command line arguments
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor to execute SQL commands and fetch results
    cursor = db.cursor()

    # Select all states, ordered by id ascending
    cursor.execute(
        "SELECT * FROM states "
        "WHERE name LIKE BINARY '{}' "
        "ORDER BY states.id ASC".format(sys.argv[4]))

    # Fetch all rows returned by the query
    rows = cursor.fetchall()

    # Print each row (each row is a tuple, e.g. (1, 'California'))
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
