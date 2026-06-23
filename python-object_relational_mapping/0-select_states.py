import MySQLdb
import sys

if __name__ == "__main__":
    argv_params = sys.argv
    if len(argv_params) < 4:
        raise ValueError("Not enough system parameter provided")
    db = MySQLdb.connect(host='localhost', user=argv_params[1], passwd=argv_params[2], db=argv_params[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    data = cur.fetchall()
    rows = [d for d in data]
    rows.sort(key=lambda row: row[0])
    for row in rows:
        print (row)