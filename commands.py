import cmd
from task_manager import *

class CLI(cmd.Cmd):
    prompt = "task-cli> "

    def __init__(self):
        super().__init__()
        create_json()

    def do_list(self, _):
        list_task()
        
    def do_add(self, arg):
        if not arg.strip():
            return
        add_task(arg)

    def do_delete(self, arg):
        if not arg.strip():
            return
        delete_task(arg)

    def do_exit(self):
        print("exiting..")
        return True
            
