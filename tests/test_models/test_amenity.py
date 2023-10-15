#!/usr/bin/python3
"""Test Amenity class"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test Amenity class"""

    def setUp(self):
        self.amenity = Amenity()

    def test_creation(self):
        self.assertEqual(self.amenity.name, '')
