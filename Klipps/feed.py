# coding: utf-8
"""
Read files.
"""

__author__ = 'Rafał Karoń <rafalkaron@gmail.com>'

def read_file_lines(file):
    """Returns a list of str lines in text file"""
    with open(file, mode="rt", encoding="utf-8") as f:
        return f.readlines()

def read_file(file):
    """Returns a string with file contents"""
    with open(file, mode='rt', encoding='utf-8') as f:
        return f.read()