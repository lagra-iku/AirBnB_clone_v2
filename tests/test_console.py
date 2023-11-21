import sys
import os
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsoleMethods(unittest.TestCase):
    """Unit tests for the HBNB Console"""

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_create_missing_class(self):
        """Test create command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_create_invalid_class(self):
        """Test create command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create InvalidClass")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_invalid_class(self):
        """Test show command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("show InvalidClass")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_missing_id(self):
        """Test show command with missing ID"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("show BaseModel")
