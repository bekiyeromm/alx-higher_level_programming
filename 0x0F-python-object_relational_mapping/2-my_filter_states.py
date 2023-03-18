#!/usr/bin/python3
"""script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where
name matches the argument"""


import MySQLdb
import sys

if __name__ == '__main__':
    # Get the MySQL login details and the state name
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    sn = sys.argv[4]
    # Connect to the database
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    # creating a cursor object using cursor() method
    cursor = db.cursor()
    # Execute the SQL query to get all states that match the user input
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                   ORDER BY id ASC".format(sn))
    # Fetch all the rows and print them out
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the database connection
    cursor.close()
    db.close()
