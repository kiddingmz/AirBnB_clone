#!/usr/bin/python3
"""Init the package"""
from models.engine import file_storage as file


storage = file.FileStorage()
storage.reload()
