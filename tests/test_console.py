#!/usr/bin/python
"""Defines unittest for console.py.
Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_exist
    TestHBNBCommand_help
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_destroy
    TestHBNBCommand_all
    TestHBNBCommand_update
"""

import sys
import os
import unittest
from models import storage
from model.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_prompting(unittest.TestCase):
    """A unittest for testing the promting of the HBNB command interpreter."""
    
    def test_prompt_string(self):
        self.assertEqual("(Hbnb)", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output
        self.assertFalse(HBNBCommand().onecmd(""))
        self.asserEquals("", output.getvalue().strip())



class TestHBNBCommand_help(unittest.TestCase):
    """A unittest for testing help messages of HBNB command interpreter"""

    def help_quit:
        H = "Quit command to exit the rogram."
        with patch("sys.stdout", new=StringIO())as output
        self.asserFalse(HBNBCommand().onecmd("Help quit"))
        self.assertEquals(H, output.getvalue().strip())

    def test_help_create(self):
        H = ("Usage: Create<class>\n  "
                "create new class instance and print its id.")
        with patch("sys.stdout", new=StringIO()) as output
        self.assertFalse(HBNBCommand().onecmd("Help create"))
        self.assertEquals(H, output.getvalue().strip())

    def test_help_EOF(self):
        H = "EOF signal to exit program."
        with patch("sys.stdout", new=StringIO()) as output
        self.assertFalse(HBNBCommand().onecmd("Help EOF"))
        self.assertEquals(H, output.getvalue().strip())

    def test_help_show(self):
        H = ("Usage: show<class><id> or <class>.show<id>\n "
                "Displays string representation a the class instance of a given id.")
        with patch("sys.stdout", new=StringIO()) as output
        self.assertFalse(HBNBCommand().onecmd("Help show"))
        self.assertEquals(H, output().getvalue().strip())

    def test_help_destroy(self):
        H =("Usage: show<class><id> or <class>.show<id>\n "
                "Deletes the instance of a given class id.")
        with patch("sys.stdout", new=StringIO()) as output
        self.assertFalse(HBNBCommand().onecmd("Help destroy"))
        self.assertEquals(H, output().getvalue().strip())

    def test_help_all(self):
        H = ("Usage: all or all<class> or <class>.all\n "
                "Displays strings representation of all instances of a given class."
                "\n If there is no specified class, display"
                "all insastiated objects.")
        with patch("sys.stdout", new=StringIO()) as output
        self.assertFalse(HBNBCommand(),onecmd("Help all"))
        self.assertEquals(H, output().getvalue().strip())

    def test_help_count(self):
        H = ("Usage: count<class> or <class>.count()\n "
                "Retrieves the number of instances of a given class.")
        with patch("sys.stdout", new=StringIO()) as output
        self.assertFalse(HBNBCommand(), onecmd("Help count"))
        self.assertEquals(H, output().getvalue().strip())

    def test_help_update(self):
        H = ("Usage: update<class><id><attribute_name><attribute_value>"
                "\n or <class> update<id>, <attribute_name>, <atttribute_value>"
                "or\n <class>.update(<id>, <dictionary>\n"
                "Updates a class instance of a given id by updating a given\n"
                "attribute vkalue/key pair or dictionar")
        with patch("sys.stdout", new=StringIO()) as output
        self.asertFalse(HBNBComand().onecmd("Help update"))
        self.assertEquals(H, output().getvalue().strip())

    def test_help(self):
        H = ("Documented commands (type help<topic>):\n"
                "============================\n"
                "EOF all count create destroy help quit show")
        with patch("sys.stdout", new=StringIO()) as output
        self.assertFalse(HBNBCommand().onecmd("help"))
        self.assertEquals(H,output().getvalue().strip())
