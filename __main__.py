# coding: utf-8
"""
Export your Kindle Clippings to a nice HTML or PDF.
"""

from Klipps import read_file, clipps_to_md, md_to_html, str_md_to_html, open_tab
import sys
import re

__version__ = "0.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

filepath = read_file(sys.argv[1])

def main():
    str_md = clipps_to_md(filepath)
    publish = str_md_to_html(str_md, "/Users/rafalkaron/GitHub/Klipps/src/")
    with open(publish, "rt") as p:
        p.read()
    print(publish)

if __name__ == "__main__":
    main()