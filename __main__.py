# coding: utf-8
"""
Export your Kindle Clippings to a nice HTML or PDF.
"""

from Klipps import read_file, clippings_to_markdown, save_file
import sys
import re

__version__ = "0.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

filepath = read_file(sys.argv[1])

def main():
    clippings_to_markdown(filepath)
    #save_file()
    

if __name__ == "__main__":
    main()