# coding: utf-8
"""
Export your Kindle Clippings to a nice HTML or PDF.
"""

from Klipps import read_file, clipps_to_md, md_to_html, str_md_to_html, open_file_tab
import sys
import re

__version__ = "0.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

file_path = read_file(sys.argv[1])
file_directory = "/Users/rafalkaron/GitHub/Klipps/src/" # it should save in the input directory. Consider using replace or re.

def main():
    str_md = clipps_to_md(file_path)
    publish = str_md_to_html(str_md, file_directory)
    open_file_tab(publish)

if __name__ == "__main__":
    main()