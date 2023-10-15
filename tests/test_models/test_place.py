#!/usr/bin/python3
"""Test Place class"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test Place class"""

    def setUp(self):
        self.place = Place()

    def test_creation(self):
        self.assertEqual(self.place.name, '')
