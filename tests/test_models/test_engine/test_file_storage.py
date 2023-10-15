#!/usr/bin/python3
"""Test FileStorage"""
from models.engine.file_storage import FileStorage
import unittest
from models.engine.file_storage import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test FileStorage"""
    def setUp(self):
        self.storage = FileStorage()

    def test_creation(self):
        self.assertEqual(self.storage.save(), None)
