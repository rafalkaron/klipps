# coding: utf-8
"""
Export your Kindle Clippings to a nice PDF.
"""

from Klipps import read_file, convert_to_markdown
import sys
import re

__version__ = "0.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

def main():
    convert_to_markdown(read_file(sys.argv[1]))

if __name__ == "__main__":
    main()