#!/usr/bin/python3
"""Test Review class"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test Review Class"""

    def setUp(self):
        self.review = Review()

    def test_creation(self):
        self.assertEqual(self.review.text, '')
