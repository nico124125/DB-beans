import database


def menu():
    connection = database.connect()
    database.create.tables(connection)

