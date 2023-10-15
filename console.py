#!/usr/bin/python3
"""Defines the Console"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Console"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Empty input"""
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
        """Creates a new instance of BaseModel
        """
        try:
            obj = eval(line.split(' ')[0])()
        except NameError:
            print("** class doesn't exist **")
        except SyntaxError:
            print("** class name missing **")
        else:
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an \
instance based on the class name and id
        """
        db = storage.all()
        kys = db.keys()
        cls_line = line.split(' ')[0]
        id_line = line.split(' ')[1]
        if "{}.{}".format(cls_line, id_line) in db:
            print(db["{}.{}".format(cls_line, id_line)])
        # obj = eval(line.split(' ')[0])()
        # print(dir(obj))
        # cls = line.split(' ')[0]
        # new_dict = obj.all()
        # id = line.split(' ')[1]
        # print(new_dict, cls, id)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        db = storage.all()
        kys = db.keys()
        cls_line = line.split(' ')[0]
        id_line = line.split(' ')[1]
        if "{}.{}".format(cls_line, id_line) in db:
            del (db["{}.{}".format(cls_line, id_line)])
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances \
based or not on the class name
        """
        db = storage.all()
        kys = db.keys()
        cls_line = line.split(' ')[0]
        bm_list = []
        for ks in kys:
            if cls_line == ks.split('.')[0]:
                bm_list.append(str(db[ks]))
        print(bm_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id \
by adding or updating attribute
        """
        db = storage.all()
        kys = db.keys()
        cls_line = line.split(' ')[0]
        id_line = line.split(' ')[1]
        key_line = line.split(' ')[2]
        val_line = line.split('"')[1]
        if "{}.{}".format(cls_line, id_line) in db:
            #print(db["{}.{}".format(cls_line, id_line)].name)
            to_up = db["{}.{}".format(cls_line, id_line)].to_dict()
            print(to_up)
            to_up[key_line] = type(to_up[key_line])(val_line)
            db["{}.{}".format(cls_line, id_line)] = to_up
            print(db["{}.{}".format(cls_line, id_line)])
            #storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
