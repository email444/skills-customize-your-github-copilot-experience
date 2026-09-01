def add_task(tasks, task):
    """Add a new task to the list."""
    pass


def show_tasks(tasks):
    """Display all tasks in a readable way."""
    pass


def save_tasks(tasks, filename):
    """Save the tasks to a text file."""
    pass


def load_tasks(filename):
    """Read tasks from a text file if it exists."""
    pass


def main():
    """Run the task manager program."""
    tasks = load_tasks("tasks.txt")

    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Save tasks")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            add_task(tasks, task)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            save_tasks(tasks, "tasks.txt")
            print("Tasks saved.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
