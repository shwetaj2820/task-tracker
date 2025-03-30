import json
import os

TASK_FILE = "task.json"

def create_json():
    """Create the task file if it does not exist."""
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, "w") as file:
            json.dump([], file, indent=4)

def load_task():
    """Load tasks from the JSON file."""
    with open(TASK_FILE, "r") as file:
        try:
            data = json.load(file)
            return data if isinstance(data, list) else []  # Ensure it's always a list
        except json.JSONDecodeError:
            return []

def save_task(task_list):
    """Save tasks to the JSON file."""
    with open(TASK_FILE, "w") as file:
        json.dump(task_list, file, indent=4)

def add_task(description):
    """Add a new task."""
    task_list = load_task()
    task_id = len(task_list) + 1
    new_task = {
        "task_id": task_id,
        "description": description,
        "status": "TODO"
    }
    task_list.append(new_task)
    save_task(task_list)

def delete_task(task_id):
    """Delete a task by ID."""
    task_list = load_task()
    task_list = [task for task in task_list if task["task_id"] != task_id]
    save_task(task_list)
