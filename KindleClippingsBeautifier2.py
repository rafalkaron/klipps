# coding: utf-8
"""
Export your Kindle Clippings to a nice PDF.
"""

__version__ = "0.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

from dirs import enter_filepath

filepath = enter_filepath()

def read(file):
    """Returns a list of str lines in text file"""
    with open(file, mode="rt", encoding="utf-8") as in_file:
        global file_lines
        file_lines = in_file.readlines()
    return file_lines

def convert_to_markdown(file_lines):
    """Marks up a list of Kindle Clipping lines with Markdown Syntax"""
    print(file_lines)

def main():
    read(filepath)
    convert_to_markdown(file_lines)

if __name__ == "__main__":
    main()