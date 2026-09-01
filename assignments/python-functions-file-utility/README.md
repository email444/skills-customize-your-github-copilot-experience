# 📘 Assignment: Python Functions & File Utility Mini-Project

## 🎯 Objective

Build a small Python program that uses functions and file handling to manage a simple to-do list. Students will practice writing reusable code, reading and writing text files, and handling basic user input in a real project.

## 📝 Tasks

### 🛠️ Create a Task Manager

#### Description
Write a program that lets a user add, view, and save tasks in a to-do list.

#### Requirements
Completed program should:

- Define at least three functions, such as `add_task()`, `show_tasks()`, and `save_tasks()`.
- Ask the user to enter a task name.
- Store each task in a list.
- Display all tasks in a clear format.
- Save the tasks to a file named `tasks.txt`.
- Load saved tasks from the file when the program starts.

### 🛠️ Use Reusable Functions

#### Description
Organize your program into small, well-named functions so the logic is easier to read and reuse.

#### Requirements
Completed program should:

- Use functions instead of writing all logic in one long block.
- Pass information into functions using parameters.
- Return values when needed.
- Keep the main program short and easy to follow.

### 🛠️ Handle Simple Errors

#### Description
Make the program more reliable by handling common user mistakes.

#### Requirements
Completed program should:

- Check whether the tasks file exists before trying to read it.
- Handle empty input gracefully.
- Display a friendly message if the list is empty.
- Avoid crashing when the user enters unexpected values.

### ✅ Example Workflow

```python
# Example of how the program may behave
Welcome to your task manager!
What would you like to do?
1. Add task
2. View tasks
3. Save tasks
4. Exit

Enter your choice: 1
Task: Review Python notes
Task added successfully.
```

### 🏁 Challenge Extension

If you finish early, add one of these features:

- Remove a task by number
- Mark a task as complete
- Show the number of tasks remaining
- Sort tasks alphabetically
