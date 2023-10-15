#!/usr/bin/python3
"""Defines the user"""
from models.base_model import BaseModel


class User(BaseModel):
    """User"""

    email = str()
    password = str()
    first_name = str()
    last_name = str()
