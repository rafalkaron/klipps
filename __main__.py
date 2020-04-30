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
                    clipps_filepath,
                    exit_prompt,
                    progressbar as pb)

__version__ = "0.7"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

def main():
    par = argparse.ArgumentParser(description="Export Kindle clippings to HTML.", formatter_class=argparse.RawTextHelpFormatter)
    par.add_argument("-in", "--input", help="Specify the \"My Clippings.txt\" file path manually.")
    par.add_argument("-out", "--output", help="Specify the HTML file path converted from the \"My Clippings.txt\" file manually.")
    par.add_argument("-nopr", "--no_preview", action="store_true", help="does not open the html file converted from the \"My Clippings.txt\" file")
    par.add_argument("-ns", "--no_style", action ="store_true", help="does not add CSS styling to the html file converted from the \"My Clippings.txt\" file")
    par.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    args = par.parse_args()
    
    if not args.input:
        in_path = clipps_filepath()
    if args.input:
        in_path = args.input

    if not args.output:
        out_path = f"{os.path.normpath(os.path.expanduser('~/Desktop'))}/{os.path.basename(in_path)}".replace(".txt", ".html").replace("\\", "/").replace("//", "/")
    if args.output:
        out_path = f"{args.output}/{os.path.basename(in_path)}".replace(".txt", ".html").replace("\\", "/").replace("//", "/")

    pb(10)
    html_str = clipps_str_to_html_str(read_file(in_path))
    pb(50)    
    if not args.no_style:
        html_str = style_html_str(html_str)
    pb(75)
    try:
        publish_html = save_str_as_file(html_str, out_path)
        pb(90)
        if not args.no_preview:
            open_file(publish_html)
        pb(100)
        print(f"Succesfully converted Kindle clippings to: \"{out_path}\"")
    except(PermissionError):
        pb(100)
        print(f"Klipps cannot save the converted Kindle clippings as: \"{out_path}\" because you lack permissions.\nTry running Klipps again as an administrator or selecting another directory.")

    exit_prompt("\nTo exit Klipps, press [Enter]")

if __name__ == "__main__":
    main()