#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa
"""
from sys import argv


if __name__ == "__main__":
    import sys
    import MySQLdb

    MY_USER, MY_PASS, MY_DB = sys.argv[1], sys.argv[2], sys.argv[3]

    conn = MySQLdb.connect(host="localhost", user=MY_USER,
                           passwd=MY_PASS, db=MY_DB)
    cur = conn.cursor()

    cur.execute(
        "SELECT cities.id, cities.name, states.name\
            FROM cities JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC"
    )

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
