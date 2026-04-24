todos = []
done = []

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

def mark_done(number):
    task = todos.pop(number - 1)
    done.append(task)
    print(f"Done: {task}")

def show_done():
    if not done:
        print("Nothing done yet.")
    for task in done:
        print(f"✓ {task}")

print("=== Simple To-Do List ===")
print("-" * 25)
add("Buy groceries")
add("Read a book")
add("Learn GitHub")
show()
print()
mark_done(3)
print("\nCompleted tasks:")
show_done()
