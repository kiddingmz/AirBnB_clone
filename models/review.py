#!/usr/bin/python3
"""Review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""
    place_id = str()
    user_id = str()
    text = str()
