#!/usr/bin/env python3
"""Test City class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test City class"""

    def setUp(self):
        self.city = City()

    def test_creation(self):
        self.assertEqual(self.city.name, '')
