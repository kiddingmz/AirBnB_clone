#!/usr/bin/python3
"""Defines the Console"""
import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        try:
            obj = eval(line.split(' ')[0])()
        except NameError:
            print("** class doesn't exist **")
        except SyntaxError:
            print("** class name missing **")
        else:
            print(obj)
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the\
                class name and id"""
        db = storage.all()
        cls = db.items()[0]
        print(cls)
       # obj = eval(line.split(' ')[0])()
       # print(dir(obj))
        #cls = line.split(' ')[0]
        #new_dict = obj.all()
        #id = line.split(' ')[1]
        #print(new_dict, cls, id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
