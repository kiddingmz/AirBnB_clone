#!/usr/bin/python3
"""Test User"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test user class"""

    def setUp(self):
        self.user = User()

    def test_creation(self):
        data = {'id' : 1,
            'fist_name' : 'Isidro',
            'last_name':'Felicio',
            'password':'123',
            'email':'isidro@felicio',
            }

        self.user = User(**data)
        self.assertEqual(self.user.id, 1)
        self.assertEqual(self.user.first_name, 'Isidro')
        self.assertEqual(self.user.first_name, 'Felicio')
        self.assertEqual(self.user.password, '123')
        self.assertEqual(self.user.email, 'isidro@felicio')
