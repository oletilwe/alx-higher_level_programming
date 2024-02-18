#!/usr/bin/python3
import MySQLdb
import sys


def list_cities_by_state(username, password, database, state_name):
    try:
        connection = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)

        cursor = connection.cursor()

        query = (
            "SELECT cities.id, cities.name, states.name "
            "FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.id ASC"
        )
        cursor.execute(query, (state_name,))

        results = cursor.fetchall()

        print("Cities:")
        for result in results:
            print(f"({result[0]}, '{result[1]}', '{result[2]}')")

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

    list_cities_by_state(username, password, database, state_name)
