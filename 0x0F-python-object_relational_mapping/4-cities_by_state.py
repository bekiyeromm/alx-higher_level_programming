#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa"""


import MySQLdb
import sys

if __name__ == '__main__':
    # Connect to MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    # creating a cursor object using cursor() method
    cursor = db.cursor()
    # Execute the SQL query to get all states that match the user input
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
            JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    # Fetch all the rows and print them out
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the database connection
    cursor.close()
    db.close()
