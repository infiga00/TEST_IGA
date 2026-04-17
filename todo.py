todos = []

def show():
    if not todos:
        print("No tasks yet.")
    for i, task in enumerate(todos, 1):
        print(f"{i}. {task}")

def add(task):
    todos.append(task)
    print(f"Added: {task}")

def remove(number):
    task = todos.pop(number - 1)
    print(f"Removed: {task}")

print("Simple To-Do List")
print("-----------------")
add("Buy groceries")
add("Read a book")
add("Learn GitHub")
show()
print()
remove(1)
show()
