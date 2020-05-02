# coding: utf-8
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

import webbrowser

def save_str_as_file(str, filepath):
    """Save a string to a file and return the file path.
    
    Keyword arguments:
    str - the string that you want to save as in a file
    filepath - the path to the file that you want to save the string to
    """
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(str)
    return filepath

def open_file(filepath):
    """Open a file in a new browser tab or in an application associated with a given file type."""
    webbrowser.open(url=f"file://{filepath}", new=2, autoraise=True)