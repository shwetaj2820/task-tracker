import sys
from commands import CLI
from task_manager import *
from utils import parse_args

def main():
    command, args = parse_args()

    if command == "add" and args:
        add_task(args)
    else:
        CLI().cmdloop()

    if command == "delete" and args:
        delete_task(args)
    else:
        CLI().cmdloop()

if __name__ == "__main__":
    main()