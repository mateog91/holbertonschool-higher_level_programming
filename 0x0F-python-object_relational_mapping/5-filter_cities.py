#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    import sys
    import MySQLdb

    MY_USER, MY_PASS, MY_DB = sys.argv[1], sys.argv[2], sys.argv[3]
    STATE = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", user=MY_USER,
                           passwd=MY_PASS, db=MY_DB)
    cur = conn.cursor()

    cur.execute(
        F"SELECT cities.id, cities.name, states.name\
            FROM cities JOIN states ON cities.state_id = states.id\
            WHERE states.name = '{STATE}'\
            ORDER BY cities.id ASC"
    )

    query_rows = cur.fetchall()
    if query_rows:
        for i in range(len(query_rows)):
            row = query_rows[i]
            if i < len(query_rows) - 1:
                print(row[1], end=", ")
            else:
                print(row[1])
    else:
        print()
    cur.close()
    conn.close()
