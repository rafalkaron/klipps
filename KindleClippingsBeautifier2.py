# coding: utf-8
"""
Export your Kindle Clippings to a nice PDF.
"""

__version__ = "0.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

from dirs import enter_filepath

filepath = enter_filepath()

def read(file):
    """Generates a list of str lines in the file"""
    with open(file, mode="rt", encoding="utf-8") as in_file:
        f = in_file.readlines()
        print(f)

def main():
    read(filepath)

if __name__ == "__main__":
    main()