# todo.py

tasks = []

def show_menu():
    print("\n📝 To-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

def add_task():
    task = input("Enter a task: ")
    tasks.append({"task": task, "done": False})
    print("✅ Task added.")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    print("\n📋 Tasks:")
    for i, task in enumerate(tasks):
        status = "✔️" if task["done"] else "❌"
        print(f"{i + 1}. {task['task']} [{status}]")

def mark_done():
    view_tasks()
    task_num = int(input("Enter task number to mark as done: "))
    if 0 < task_num <= len(tasks):
        tasks[task_num - 1]["done"] = True
        print("✅ Task marked as done.")
    else:
        print("❌ Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        print("👋 Exiting. Stay productive!")
        break
    else:
        print("Invalid choice. Try again.")
