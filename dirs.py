# coding: utf-8
"""
Manage your local directories.
"""

__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

import os
import sys

def exe_dir():
    """Returns the directory of the executable. Works after compilation."""
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    elif __file__:
        return os.path.dirname(__file__)

def enter_filepath():
    """Prompts you to provide a full path to a file"""
    return input("Enter a full path to the file: ")