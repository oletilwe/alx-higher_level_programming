#!/usr/bin/python3
import MySQLdb
import sys


def search_state(username, password, database, state_name):
    try:
        connection = MySQLdb.connect(
            host='localhost', port=3306,
            user=username, passwd=password, db=database
        )

        cursor = connection.cursor()

        query = (
            "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        )
        cursor.execute(query, (state_name,))

        results = cursor.fetchall()

        print("Results:")
        for result in results:
            print(f"ID: {result[0]}, Name: {result[1]}, Abbreviation: {result[2]}")

    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]

    search_state(username, password, database, state_name)
