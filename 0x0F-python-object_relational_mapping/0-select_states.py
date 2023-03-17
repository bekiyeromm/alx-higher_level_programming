#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa
#usage ./0-select_states.py root root hbtn_0e_0_usa"""


import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    state = cursor.fetchall()

    for st in state:
        print(st)
