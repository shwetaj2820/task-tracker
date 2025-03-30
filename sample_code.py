import cmd
import json
import os
from datetime import datetime


TASK_FILE = "task.json"


class CLI(cmd.Cmd):
    """Task Tracker CLI"""
    prompt = "task-cli> "
    intro = "Welcome to Task Tracker! Type 'help' for available commands."

    def __init__(self):
        super().__init__()
        self.init_task_file()

    @staticmethod
    def init_task_file():
        """Initialize the task file if it doesn't exist"""
        if not os.path.exists(TASK_FILE):
            with open(TASK_FILE, "w") as file:
                json.dump([], file, indent=4)

    def load_tasks(self):
        """Load tasks from JSON file"""
        with open(TASK_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []

    def save_tasks(self, tasks):
        """Save tasks to JSON file"""
        with open(TASK_FILE, "w") as file:
            json.dump(tasks, file, indent=4)

    def do_add(self, arg):
        """Add a new task: add <description>"""
        if not arg:
            print("❌ Task description required!")
            return
        tasks = self.load_tasks()
        task_id = len(tasks) + 1
        new_task = {
            "task_id": task_id,
            "description": arg,
            "status": "todo",
            "createdAt": str(datetime.now()),
            "updatedAt": str(datetime.now())
        }
        tasks.append(new_task)
        self.save_tasks(tasks)
        print(f"✅ Task added successfully (ID: {task_id})")

    def do_list(self, arg):
        """List all tasks or filter by status: list [status]"""
        tasks = self.load_tasks()
        if arg:
            tasks = [t for t in tasks if t["status"] == arg]
        if not tasks:
            print("No tasks found.")
            return
        for task in tasks:
            print(f"[{task['task_id']}] {task['description']} - {task['status']}")

    def do_update(self, arg):
        """Update task description: update <task_id> <new_description>"""
        args = arg.split(" ", 1)
        if len(args) < 2:
            print("❌ Usage: update <task_id> <new_description>")
            return
        task_id, new_desc = int(args[0]), args[1]
        tasks = self.load_tasks()
        for task in tasks:
            if task["task_id"] == task_id:
                task["description"] = new_desc
                task["updatedAt"] = str(datetime.now())
                self.save_tasks(tasks)
                print(f"✅ Task {task_id} updated successfully")
                return
        print(f"❌ Task {task_id} not found!")

    def do_delete(self, arg):
        """Delete a task: delete <task_id>"""
        if not arg.isdigit():
            print("❌ Usage: delete <task_id>")
            return
        task_id = int(arg)
        tasks = self.load_tasks()
        tasks = [t for t in tasks if t["task_id"] != task_id]
        self.save_tasks(tasks)
        print(f"✅ Task {task_id} deleted successfully")

    def do_mark(self, arg):
        """Mark task as done or in-progress: mark <task_id> <done/in-progress>"""
        args = arg.split(" ")
        if len(args) < 2:
            print("❌ Usage: mark <task_id> <done/in-progress>")
            return
        task_id, status = int(args[0]), args[1]
        if status not in ["done", "in-progress"]:
            print("❌ Status must be 'done' or 'in-progress'")
            return
        tasks = self.load_tasks()
        for task in tasks:
            if task["task_id"] == task_id:
                task["status"] = status
                task["updatedAt"] = str(datetime.now())
                self.save_tasks(tasks)
                print(f"✅ Task {task_id} marked as {status}")
                return
        print(f"❌ Task {task_id} not found!")

    def do_exit(self, arg):
        """Exit the Task Tracker CLI"""
        print("Goodbye! 👋")
        return True


if __name__ == "__main__":
    CLI().cmdloop()
