#!/usr/bin/python3
"""Defines the Console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Console"""
    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Quit command to exit the program
        """
        self.do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
