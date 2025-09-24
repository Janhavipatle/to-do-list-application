# todo.py

TASKS_FILE = "tasks.txt"

# Function to load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            tasks = f.read().splitlines()
    except FileNotFoundError:
        tasks = []
    return tasks

# Function to save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Function to display tasks
def view_tasks(tasks):
    if not tasks:
        print("\n✅ No tasks available!\n")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

# Main program
def main():
    tasks = load_tasks()

    while True:
        print("==== TO-DO LIST MENU ====")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            new_task = input("Enter new task: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)
                print("✅ Task added!\n")
            else:
                print("⚠️ Empty task cannot be added.\n")

        elif choice == "3":
            view_tasks(tasks)
            try:
                task_num = int(input("Enter task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"❌ Removed: {removed}\n")
                else:
                    print("⚠️ Invalid task number.\n")
            except ValueError:
                print("⚠️ Please enter a valid number.\n")

        elif choice == "4":
            print("👋 Exiting... Your tasks are saved!")
            break

        else:
            print("⚠️ Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
