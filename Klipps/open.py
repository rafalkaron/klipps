# coding: utf-8
"""
Open files.
"""

__author__ = 'Rafał Karoń <rafalkaron@gmail.com>'

import webbrowser

def open_file_tab(url):
    """Opens a file in a new browser tab or in an app associated with a given filetype in your OS."""
    webbrowser.open(url=f"file://{url}", new=2, autoraise=True)