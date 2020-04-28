# coding: utf-8
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

def read_file(filepath):
    """Return a string with file contents."""
    with open(filepath, mode='rt', encoding='utf-8') as f:
        return f.read()