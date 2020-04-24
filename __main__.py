# coding: utf-8
"""
Export a \"My Clippings.txt\" Kindle file to HTML5.
"""

import sys
import re
import os
from Klipps import (read_file,
                    clipps_to_md,
                    md_str_to_html_str,
                    style_html_str,
                    save_str_as_file,
                    open_file_tab,
                    md_str_to_md)

__version__ = "0.2"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

clipps_path = read_file(sys.argv[1])
clipps_directory = os.path.dirname(os.path.abspath(sys.argv[1]))

def main():
    # Add help info if you open an app without an argument
    md_str = clipps_to_md(clipps_path)
    md_str_to_md(md_str, clipps_directory)
    html_str = md_str_to_html_str(md_str)
    html_str = style_html_str(html_str)
    publish_html5 = save_str_as_file(html_str, f"{clipps_directory}/My Clippings.html")
    open_file_tab(publish_html5)

if __name__ == "__main__":
    main()