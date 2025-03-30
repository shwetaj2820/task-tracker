import cmd
from task_manager import add_task, delete_task, load_task, create_json

class CLI(cmd.Cmd):
    prompt = "task-cli> "

    def __init__(self):
        super().__init__()
        create_json()

    def do_add(self, arg):
        """Add a task: add <description>"""
        if not arg.strip():
            print("Task description cannot be empty!")
            return
        add_task(arg)
        print(f"Task added: {arg}")

    def do_delete(self, arg):
        """Delete a task by ID: delete <task_id>"""
        try:
            task_id = int(arg)
            delete_task(task_id)
            print(f"Task {task_id} deleted.")
        except ValueError:
            print("Please provide a valid task ID.")

    def do_list(self, _):
        """List all tasks."""
        tasks = load_task()
        if not tasks:
            print("No tasks found.")
            return
        for task in tasks:
            print(f"{task['task_id']}: {task['description']} [{task['status']}]")

    def do_exit(self, _):
        """Exit the CLI."""
        print("Exiting task manager.")
        return True
