#!/usr/bin/python3
"""Defines the file storage"""
import os


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
        self.__file_path = "storage.json"
        with open(self.__file_path, "a+") as file:
            file.write(self.__objects)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                file.read(loads(self.__objects))
