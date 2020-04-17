"""
Manage directories in your OS.
"""

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

def main():
    exe_dir()

if __name__ == "__main__":
    main()