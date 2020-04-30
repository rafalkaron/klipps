# coding: utf-8
"""
Export a \"My Clippings.txt\" Kindle file to HTML5.
"""

import sys
import re
import os
import argparse
from Klipps import (read_file,
                    clipps_str_to_html_str,
                    style_html_str,
                    save_str_as_file,
                    open_file,
                    progressbar as pb)

__version__ = "0.6"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

def main():
    par = argparse.ArgumentParser(description="Export Kindle clippings to HTML.", formatter_class=argparse.RawTextHelpFormatter)
    par.add_argument("kindle_clippings_path", help="The file path to the \"My Clippings.txt\" file that you want to convert to HTML.\nFor example: \"D:\Kindle\Documents\My Clippings.txt\" (Windows) or \"/Volumes/Kindle/documents/My Clippings.txt\" (macOS).\nNote: Remember to encapsulate the path in inverted commas!")
    par.add_argument("-nopr", "--no_preview", action="store_true", help="does not open the html file converted from the \"My Clippings.txt\" file")
    par.add_argument("-ns", "--no_style", action ="store_true", help="does not add CSS styling to the html file converted from the \"My Clippings.txt\" file")
    par.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    if len(sys.argv)==1:
        par.print_help(sys.stderr)
        sys.exit(1)
    args = par.parse_args()
    
    pb(10)
    html_str = clipps_str_to_html_str(read_file(args.kindle_clippings_path))
    pb(25)
    html_path = args.kindle_clippings_path.replace(".txt", ".html")
    pb(50)    
    if not args.no_style:
        html_str = style_html_str(html_str)
    pb(75)
    publish_html5 = save_str_as_file(html_str, html_path)
    pb(90)
    if not args.no_preview:
        open_file(publish_html5)
    pb(100)
    print(f"Succesfully converted Kindle Clippings to: \"{html_path}\"")

if __name__ == "__main__":
    main()