#!/usr/bin/python3
"""This module contains the BaseModel class"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """Defines common attributes/methods for hbnb classes"""

    def __init__(self, *args, **kwargs):
        """"BaseModel constructor"""
        for key, val in kwargs.items():
            if key == '__class__':
                continue
            if key == 'created_at' or key == 'updated_at':
                setattr(self, key, datetime.fromisoformat(val))
                continue
            setattr(self, key, val)
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        models.storage.new(self)    

    def __str__(self):
        """Prints the string format representation of a BaseModel object"""
        return ("[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__))

    def save(self):
        """Save BaseModel object data into file"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Maps the object's attributes into a dictionary

        Returns:
            A dictionary containing all keys/values"""
        # new_dict = {'__class__': type(self).__name__}
        new_dict = {**self.__dict__}
        new_dict['__class__'] = type(self).__name__
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['created_at'] = self.created_at.isoformat()
        return (new_dict)
