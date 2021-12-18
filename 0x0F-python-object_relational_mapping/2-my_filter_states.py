#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    import sys
    import MySQLdb

    MY_USER, MY_PASS, MY_DB = sys.argv[1], sys.argv[2], sys.argv[3]
    state = argv[4]

    conn = MySQLdb.connect(host="localhost", user=MY_USER,
                           passwd=MY_PASS, db=MY_DB)
    cur = conn.cursor()
    cur.execute(
        f"SELECT * FROM states WHERE name = '{state}'")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
