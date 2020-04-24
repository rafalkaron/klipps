# coding: utf-8
"""
Export a \"My Clippings.txt\" Kindle file to HTML5.
"""

import sys
import re
import os
import argparse
from Klipps import (read_file,
                    clipps_str_to_md_str,
                    md_str_to_html_str,
                    style_html_str,
                    save_str_as_file,
                    open_file,
                    md_str_to_md,
                    cli)

__version__ = "0.3"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

def main():
    parser = argparse.ArgumentParser(description="Convert your Kindle clippings to HTML.")
    parser.add_argument('clipps_path', help=r'A file path to the "My Clippings.txt" file on your Kindle device that you want to convert to HTML. For example: "D:\Kindle\Documents\My Clippings.txt" (Windows) or "/Volumes/Kindle/documents/My Clippings.txt" (macOS). Remember to encapsulate the path in inverted commas!')
    parser.add_argument("-md", '--markdown', action="store_true", help='In addition to HTML, converts your "My Clippings.txt" file to Markdown.')
    parser.add_argument("-nopr", "--no_preview", action="store_true", help="Prevents the converted files from opening.")
    args = parser.parse_args()
    
    clipps_directory = os.path.dirname(os.path.abspath(args.clipps_path))
    md_str = clipps_str_to_md_str(read_file(args.clipps_path))
    
    html_str = md_str_to_html_str(md_str)
    html_str = style_html_str(html_str)
    
    publish_html5 = save_str_as_file(html_str, f"{clipps_directory}/My Clippings.html")

    if not args.no_preview:
        open_file(publish_html5)

    if args.markdown:
        md_str_to_md(md_str, clipps_directory)

if __name__ == "__main__":
    main()