#!/usr/bin/python3
"""
    Get all states of a data base
"""
import MySQLdb
from sys import argv


def main():
    """Only executes when is not imported"""
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         port=3306,
                         passwd=argv[2],
                         db=argv[3])
    c = db.cursor()
    numrows = c.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    states = c.fetchall()
    for ids, state in states:
        print(ids, state)

if __name__ == "__main__":
    main()
