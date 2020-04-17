# coding: utf-8
"""

"""

def read_file_lines(file):
    """Returns a list of str lines in text file"""
    with open(file, mode="rt", encoding="utf-8") as in_file:
        file_lines = in_file.readlines()
    return file_lines