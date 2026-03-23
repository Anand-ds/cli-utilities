FILE = "data/todos.txt"

def show_tasks():
    try:
        with open(FILE, "r") as f:
            tasks = f.readlines()
            if not tasks:
                print("No tasks yet.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks file found yet.")

def add_task():
    task = input("Enter new task: ")
    with open(FILE, "a") as f:
        f.write(task + "\n")
    print("Task added!")

def delete_task():
    show_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1

        with open(FILE, "r") as f:
            tasks = f.readlines()

        if 0 <= index < len(tasks):
            tasks.pop(index)

            with open(FILE, "w") as f:
                f.writelines(tasks)

            print("Task deleted!")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")

def todo_menu():
    while True:
        print("\n--- To-Do List ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Back")

        choice = input("Choose: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            break
        else:
            print("Invalid choice.") 
