import cmd
# import json
# filename = data.json

class CLI(cmd.Cmd):
    prompt=">> "
    intro="Welcome to task tracker. Type 'help' for list of all commands"


if __name__=="__main__":
    cli = CLI()
    cli.cmdloop()