#!/usr/bin/python3
"""Defines the file storage"""
import os
from json import load, dump, dumps, loads
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from datetime import datetime


class FileStorage():
    """Class File Storage"""
    __file_path = str()
    __objects = dict()

    def all(self):
        """Return the dictionary"""
        return (self.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = type(obj).__name__+'.'+obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        output = {k: v.to_dict() for k, v in self.__objects.items()}
        self.__file_path = "storage.json"
        with open(self.__file_path, "w") as file:
            dump(output, file)
            file.write(str('\n'))

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file"""
        self.__file_path = "storage.json"
        if os.path.exists(self.__file_path):
            with open(self.__file_path) as file:
                new_dict = load(file)
                for v in new_dict.values():
                    cls = v['__class__']
                    del (v['__class__'])
                    self.new(eval(cls)(**v))
