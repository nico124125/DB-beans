import sqlite3


CREATE_PLANE_TABLE = "CREATE TABLE IF NOT EXISTS planes (id INTEGER PRIMARY KEY, name TEXT, method TEXT, rating INTEGER);"

INSERT_PLANE = "INSERT INTO planes (name, method, rating) VALUES (?, ?, ?);"
DELETE_PLANE_BY_NAME = "DELETE FROM planes WHERE name = ?;"
GET_ALL_PLANES = "SELECT * FROM planes;"
GET_PLANES_BY_NAME = "SELECT * FROM planes WHERE name = ?;"
DELETE_PLANE_BY_ID = "DELETE FROM plane WHERE id"
GET_BEST_PREPARATION_FOR_PLANE = """
SELECT * FROM planes
WHERE name = ?
ORDER BY rating DESC
LIMIT 1;"""


def connect():
    return sqlite3.connect("data.db")


def create_tables(connection):
    with connection:
        connection.execute(CREATE_PLANE_TABLE)


def add_plane(connection, name, method, rating):
    with connection:
        connection.execute(INSERT_PLANE, (name, method, rating))



def get_all_planes(connection):
    with connection:
        return connection.execute(GET_ALL_PLANES).fetchall()


def get_planes_by_name(connection, name):
    with connection:
        return connection.execute(GET_PLANES_BY_NAME, (name,)).fetchall()

def get_best_preparation_for_plane(connection, name):
    with connection:
        return connection.execute(GET_BEST_PREPARATION_FOR_PLANE, (name, )).fetchone()

def delete_plane_by_name(connection, name):
    with connection:
        return connection.execute(DELETE_PLANE_BY_NAME, (name, ))

def delete_plane_by_id(connection, name):
    with connection:
        return connection.execute(DELETE_PLANE_BY_ID, (name, ))
