#!/usr/bin/python3
"""Write a script that takes in the name of a state as
an argument and lists all cities of that state, using
the database hbtn_0e_4_usa"""


import MySQLdb
import sys

if __name__ == '__main__':
    # Get the state name
    sn = sys.argv[4]
    # Connect to the database
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    # creating a cursor object using cursor() method
    cursor = db.cursor()
    # Execute the SQL query to get all states that match the user input
    cursor.execute("SELECT cities.name FROM cities\
            JOIN states ON cities.state_id = states.id WHERE states.name=%s\
            ORDER BY cities.id ASC", (sn,))
    # Fetch all the rows and print them out
    cities = cursor.fetchall()
    print(", ".join(city[0] for city in cities))

    # Close the database connection
    cursor.close()
    db.close()
