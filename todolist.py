def menu(menu_items):
    while True:
        print(menu_items)
def create_task():
    pass
def delete_task():
    pass
def view_tasks():
    pass


menu_selection = [
    str(input("Create Task press 1: ")), str(input("Delete Task press 2: ")), str(input("View Tasks press 3: "))
]

menu(menu_selection)