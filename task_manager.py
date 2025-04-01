import json
import os

TASK_FILE = "task.json"

def create_json():
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, "w") as file:
            json.dump([], file, indent=4)

def load_task():
    with open(TASK_FILE, "r") as file:
        try:
            data = json.load(file)
            return data if isinstance(data, list) else []  
        except json.JSONDecodeError:
            return []

def save_task(task_list):
    with open(TASK_FILE, "w") as file:
        json.dump(task_list, file, indent=4)

def add_task(description):
    task_list = load_task()
    task_id = len(task_list) + 1
    new_task = {
        "task_id": task_id,
        "description": description,
    }
    task_list.append(new_task)
    save_task(task_list)

def delete_task(task_id):
    task_id = int(task_id)
    tasks = load_task()
    tasks = [t for t in tasks if t["task_id"] != task_id]
    save_task(tasks)

def list_task():
    tasks = load_task()
    if not tasks:
        return
    for task in tasks:
        print(f"{task['task_id']}: {task['description']}")
