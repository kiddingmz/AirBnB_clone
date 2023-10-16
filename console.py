#!/usr/bin/python3
"""Defines the Console"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Console"""
    prompt = "(hbnb) "
    valid_classes = ['BaseModel', 'User', 'Amenity', 'Review', 'State', 'City',
                     'Place']
    ERROR_CLASS_NAME = '** class name missing **'
    ERROR_CLASS = "** class doesn't exist **"
    ERROR_ID = "** instance id missing **"
    ERROR_ID_NOT_FOUND = "** no instance found **"
    ERROR_ATTR = "** attribute name missing **"
    ERROR_ATTR_VALUE = "** value missing **"

    def onecmd(self, line):
        spliter = line.split(".")
        if len(spliter) > 1:
            cls_name = spliter[0]
            command = spliter[1].replace('()', '')
            
            if cls_name in self.valid_classes:
                line = "{} {}".format(command, cls_name)
        return super().onecmd(line)

    def validate_len_args(self, line):
        if len(line) == 0:
            print(self.ERROR_CLASS_NAME)
            return False
        return True

    def validate_class_name(self, line):
        args = line.split(' ')
        class_name = args[0]
        if class_name not in self.valid_classes:
            print(self.ERROR_CLASS)
            return False
        return class_name

    def validate_id(self, line):
        args = line.split(' ')
        if len(args) < 2:
            print(self.ERROR_ID)
            return False
        id_number = args[1]
        return id_number

    def validate_attr(self, line):
        args = line.split(' ')
        if len(args) < 3:
            print(self.ERROR_ATTR)
            return False
        attribute = args[2]
        return attribute

    def validate_attr_value(self, line):
        args = line.split(' ')
        if len(args) < 4:
            print(self.ERROR_ATTR_VALUE)
            return False
        attr_value = args[3]
        return attr_value

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
        print()
        self.do_quit

    def do_create(self, line):
        """Creates a new instance of BaseModel
        """
        '''try:
            obj = eval(line.split(' ')[0])()
        except NameError:
            print("** class doesn't exist **")
        except SyntaxError:
            print("** class name missing **")
        else:
            obj.save()
            print(obj.id)
        '''
        if not self.validate_len_args(line):
            return

        cls_name = self.validate_class_name(line)
        if not cls_name:
            return

        obj = eval(cls_name)()
        obj.save()
        print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an \
instance based on the class name and id
        """
        if not self.validate_len_args(line):
            return

        cls_name = self.validate_class_name(line)
        if not cls_name:
            return

        id_line = self.validate_id(line)
        if not id_line:
            return

        db = storage.all()
        if "{}.{}".format(cls_name, id_line) in db:
            print(db["{}.{}".format(cls_name, id_line)])
        else:
            print(self.ERROR_ID_NOT_FOUND)
        # obj = eval(line.split(' ')[0])()
        # print(dir(obj))
        # cls = line.split(' ')[0]
        # new_dict = obj.all()
        # id = line.split(' ')[1]
        # print(new_dict, cls, id)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        if not self.validate_len_args(line):
            return

        cls_name = self.validate_class_name(line)
        if not cls_name:
            return

        id_line = self.validate_id(line)
        if not id_line:
            return

        db = storage.all()
        if "{}.{}".format(cls_name, id_line) in db:
            del (db["{}.{}".format(cls_name, id_line)])
            storage.save()
        else:
            print(self.ERROR_ID_NOT_FOUND)

    def do_all(self, line):
        """Prints all string representation of all instances \
based or not on the class name
        """
        db = storage.all()
        kys = db.keys()
        cls_line = self.validate_class_name(line)
        bm_list = list()
        for ks in kys:
            if cls_line == ks.split('.')[0]:
                bm_list.append(str(db[ks]))
        if len(bm_list) > 0:
            print(bm_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id \
by adding or updating attribute
        """
        if not self.validate_len_args(line):
            return

        cls_line = self.validate_class_name(line)
        if not cls_line:
            return

        id_line = self.validate_id(line)
        if not id_line:
            return

        key_line = self.validate_attr(line)
        if not key_line:
            return

        val_line = self.validate_attr_value(line)
        if not val_line:
            return

        db = storage.all()
        kys = db.keys()
        if "{}.{}".format(cls_line, id_line) in db:
            if val_line.isdigit():
                val_line = int(val_line)
            else:
                try:
                    val_line = float(val_line)
                except:
                    pass

            setattr(db["{}.{}".format(cls_line, id_line)], key_line, val_line)
            storage.save()
        else:
            print(self.ERROR_ID_NOT_FOUND)

    def do_count(self, line):
        """Number of instances of a class: <class name>.count()"""
        if not self.validate_len_args(line):
            return

        cls_name = self.validate_class_name(line)
        if not cls_name:
            return

        db = storage.all()
        i = 0
        for k, v in db.items():
            if k.split('.')[0] == cls_name:
                i += 1
        print(i)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
