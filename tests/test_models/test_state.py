#!/usr/bin/env python3
"""Test State Class"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test State class"""

    def setUp(self):
        self.state = State()

    def test_creation(self):
        self.assertEqual(self.State.name, '')
