#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsoleMethods(unittest.TestCase):
    """Test methods in the HBNBCommand console"""

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_instance(self, mock_stdout):
        """Test create method to create an instance"""
        HBNBCommand().onecmd('create BaseModel')
        output = mock_stdout.getvalue().strip()
        self.assertNotEqual(output, '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_existing_instance(self, mock_stdout):
        """Test show method with an existing instance"""
        HBNBCommand().onecmd('create BaseModel')
        output = mock_stdout.getvalue().strip()
        instance_id = output.split()[-1]  # Assuming ID is printed at the end
        HBNBCommand().onecmd(f'show BaseModel {instance_id}')
        show_output = mock_stdout.getvalue().strip()
        self.assertNotEqual(show_output, '** no instance found **')

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_non_existing_instance(self, mock_stdout):
        """Test show method with a non-existing instance"""
        HBNBCommand().onecmd('show BaseModel invalid_id')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '** no instance found **')

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_existing_instance(self, mock_stdout):
        """Test destroy method with an existing instance"""
        HBNBCommand().onecmd('create BaseModel')
        output = mock_stdout.getvalue().strip()
        instance_id = output.split()[-1]  # Assuming ID is printed at the end
        HBNBCommand().onecmd(f'destroy BaseModel {instance_id}')
        destroy_output = mock_stdout.getvalue().strip()
        self.assertNotEqual(destroy_output, '** no instance found **')

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_non_existing_instance(self, mock_stdout):
        """Test destroy method with a non-existing instance"""
        HBNBCommand().onecmd('destroy BaseModel invalid_id')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '** no instance found **')

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_existing_instance(self, mock_stdout):
        """Test update method with an existing instance"""
        HBNBCommand().onecmd('create BaseModel')
        output = mock_stdout.getvalue().strip()
        instance_id = output.split()[-1]  # Assuming ID is printed at the end
        HBNBCommand().onecmd(f'update BaseModel {instance_id} name "NewName"')
        update_output = mock_stdout.getvalue().strip()
        self.assertNotEqual(update_output, '** no instance found **')

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_non_existing_instance(self, mock_stdout):
        """Test update method with a non-existing instance"""
        HBNBCommand().onecmd('update BaseModel invalid_id')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, '** no instance found **')


if __name__ == '__main__':
    unittest.main()
