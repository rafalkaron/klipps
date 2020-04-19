# coding: utf-8
"""
Perform common actions with a web browser
"""

__author__ = 'Rafał Karoń <rafalkaron@gmail.com>'

import webbrowser

def open_tab(url):
    """Opens an URL in a new tab of your default web browser. You need to include the protocol in the URL."""
    webbrowser.open(url=url, new=1, autoraise=True)