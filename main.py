import json
import os

TASK_FILE = "tasks.json"

# Load tasks from json file
def load_task():
    if not os.path.exists(TASK_FILE):
        return [], 0  # Return empty list and highest ID as 0

    with open(TASK_FILE, "r") as file:
        try:
            tasks = json.load(file)
            max_id = max([n["id"] for n in tasks], default=0)
            return tasks, max_id  # Corrected return statement
        except json.JSONDecodeError:
            return [], 0  # If file is empty or corrupted

# Save tasks to json file
def save_task(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add new task
def add_task():
    tasks, highest_id = load_task()  # Load tasks and max ID
    description = input("Enter task description: ")
    task_id = highest_id + 1  # Assign the next available ID

    new_task = {
        "id": task_id,
        "description": description,  # Fixed key name from "descreption"
        "completed": False
    }

    tasks.append(new_task)
    save_task(tasks)
    print(f"Task added: {description}")

# List all tasks
def list_task():
    tasks, _ = load_task()
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "✅" if task["completed"] else "❌"
        print(f"{task['id']}: {task['description']} -- {status}")

# Mark a task as completed
def completed_task(task_id):
    tasks, _ = load_task()
    task_found = False

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            task_found = True
            break

    if task_found:
        save_task(tasks)
        print(f"Task {task_id} marked as completed")
    else:
        print(f"Task {task_id} not found")

# Delete a task
def delete_task(task_id):
    tasks, _ = load_task()
    updated_tasks = [task for task in tasks if task["id"] != task_id]

    if len(updated_tasks) == len(tasks):
        print(f"Task {task_id} not found")
    else:
        save_task(updated_tasks)
        print(f"Task {task_id} deleted successfully")

# CLI Menu using match-case (Python 3.10+)
if __name__ == "__main__":
    while True:
        print("\nTask Manager:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        match choice:
            case "1":
                add_task()
            case "2":
                list_task()
            case "3":
                task_id = int(input("Enter task ID to mark as completed: "))
                completed_task(task_id)
            case "4":
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
            case "5":
                print("Exiting Task Manager. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")
