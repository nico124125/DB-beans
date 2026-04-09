import database


MENU_PROMPT = """--- Military Plane Rating ---

Please choose one of these options:

1) Add a new plane.
2) See all planes.
3) Find a plane by name.
4) See which role is best for plane. 
5) delete plane
6) delete plane by ID
7) Exit.

Your selection: """


def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "7":
        if user_input == "1":
            prompt_add_new_plane(connection)
        elif user_input == "2":
            prompt_see_all_planes(connection)
        elif user_input == "3":
            prompt_find_plane(connection)
        elif user_input == "4":
            prompt_find_best_method(connection)
        elif user_input == "5":
            prompt_delete_plane(connection)
        elif user_input == "6":
            prompt_delete_plane_by_id(connection)
        else:
            print("Invalid input, please try again")

def prompt_add_new_plane(connection):
    name = input("Enter plane: ")
    method = input("Enter the plane's role (Bomber, Fighter etc): ")
    rating = int(input("Enter score (0-100): "))

    database.add_plane(connection, name, method, rating)

def prompt_see_all_planes(connection):
    planes = database.get_all_planes(connection)

    for plane in planes:
        print(f"ID: {plane[0]} | {plane[1]} ({plane[2]}) - {plane[3]}/100")

def prompt_find_plane(connection):
    name = input("Enter plane name to find: ")
    plane = database.get_planes_by_name(connection, name)

    for plane in plane:
        print(f"ID: {plane[0]} | {plane[1]} ({plane[2]}) - {plane[3]}/100")

def prompt_find_best_method(connection):
    name = input("Enter plane name to find: ")
    best_method = database.get_best_preparation_for_plane(connection, name)

def prompt_delete_plane(connection):
    name = input("Enter plane name to delete: ")
    delete = database.delete_plane_by_name(connection, name)

def prompt_delete_plane_by_id(connection):
    plane_id = input("Enter plane ID to delete: ")
    delete = database.delete_plane_by_id(connection, plane_id)




menu()
