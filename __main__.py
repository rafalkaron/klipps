# coding: utf-8
"""
Export your Kindle Clippings to a nice HTML or PDF.
"""

import sys
import re
import os
from Klipps import (read_file,
                    clipps_to_md,
                    md_str_to_html,
                    open_file_tab,
                    md_str_to_md)

__version__ = "0.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

clipps_path = read_file(sys.argv[1])
clipps_directory = os.path.dirname(os.path.abspath(sys.argv[1]))

def main():
    md_str = clipps_to_md(clipps_path)
    publish_html5 = md_str_to_html(md_str, clipps_directory)
    md_str_to_md(md_str, clipps_directory)
    open_file_tab(publish_html5)
    
if __name__ == "__main__":
    main()