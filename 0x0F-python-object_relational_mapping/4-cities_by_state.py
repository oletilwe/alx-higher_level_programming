#!/usr/bin/python3
import MySQLdb
import sys


def list_cities(username, password, database):
    try:
        connection = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)

        cursor = connection.cursor()

        query = "SELECT * FROM cities ORDER BY id ASC"
        cursor.execute(query)

        results = cursor.fetchall()

        print("Cities:")
        for result in results:
            print(f"{result[0]}: ({result[1]}, '{result[2]}')")

    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1:]

    list_cities(username, password, database)
