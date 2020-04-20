# coding: utf-8
"""
Export your Kindle Clippings to a nice HTML or PDF.
"""

from Klipps import read_file, clipps_to_md, md_to_html, md_str_to_html_css, open_file_tab, md_str_to_md
import sys
import re

__version__ = "0.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

file_path = read_file(sys.argv[1])
file_directory = "/Users/rafalkaron/GitHub/Klipps/src/" # it should save in the input directory. Consider using replace or re.

def main():
    md_str = clipps_to_md(file_path)
    
    publish_html5 = md_str_to_html_css(md_str, file_directory)
    open_file_tab(publish_html5)
    
    publish_md = md_str_to_md(md_str, file_directory)
    open_file_tab(publish_md)



if __name__ == "__main__":
    main()