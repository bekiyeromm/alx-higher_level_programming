#!/usr/bin/python3
""" lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa
usage ./1-filter_states.py root root hbtn_0e_0_usa"""


import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    state = cursor.fetchall()

    for st in state:
        if st[1][0] == 'N':
            print(st)
    cursor.close()
    conn.close()
