#!/usr/bin/python3
"""This module contains the BaseModel class"""
from datetime import datetime
import uuid


class BaseModel:
    """Defines common attributes/methods for hbnb classes"""

    def __init__(self):
        """"BaseModel constructor"""
        id = str(uuid.uuid4())
        created_at = datetime.now().isoformat()
        updated_at = datetime.now().isoformat()

    def __str__(self):
        """Prints the string format representation of a BaseModel object"""
        print("[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__))

    def save(self):
        """Save BaseModel object data into file"""
        self.updated_at = datetime.now().isoformat()
