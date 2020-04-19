# coding: utf-8
"""
Export your Kindle Clippings to a nice PDF.
"""

from Klipps import read_file
import sys
import re

__version__ = "0.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

clippings = read_file(sys.argv[1])

def convert_to_markdown(file):
    """Applies Markdown syntax to a raw \"Kindle Clippings.txt file\""""    
    print(clippings)
    
def main():
    convert_to_markdown(clippings)

if __name__ == "__main__":
    main()