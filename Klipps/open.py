# coding: utf-8
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

import webbrowser

def open_file(filepath):
    """Open a file in a new browser tab or in an application associated with a given file type."""
    webbrowser.open(url=f"file://{filepath}", new=2, autoraise=True)