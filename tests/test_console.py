#!/usr/bin/python3
"""module documentation"""
import unittest
from models.base_model import BaseModel
import os
import sys
from console import HBNBCommand
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    """test HBNBCommand class"""
    def setUp(self) -> None:
        return super().setUp()

    def out_test(self, func, arg, expect):
        """test commands of the console"""
        std_out = StringIO()
        sys.stdout = std_out
        func(arg)
        output = std_out.getvalue()
        self.assertEqual(output, expect + '\n')
        return output

    def test_creation_failed(self):
        """create command of the console"""
        try:
            os.remove('storage.json')
        except FileNotFoundError:
            pass
        cmd = HBNBCommand()

        self.out_test(cmd.do_create, '', HBNBCommand.ERROR_CLASS_NAME)
        self.out_test(cmd.do_create, 'myModel', HBNBCommand.ERROR_CLASS)
