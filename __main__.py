# coding: utf-8
"""
Export a \"My Clippings.txt\" Kindle file to HTML5.
"""

import sys
import re
import os
import argparse
from Klipps import (clipps_filepath,
                    read_file,
                    progressbar as pb,
                    clipps_str_to_html_str,
                    style_html_str,
                    save_str_as_file,
                    open_file,
                    exit_prompt)

__version__ = "0.7"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

def main():
    par = argparse.ArgumentParser(description="Export clippings from Kindle to a HTML file on your desktop.", formatter_class=argparse.RawTextHelpFormatter)
    par.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    par.add_argument("-in", "--input", metavar="clippings_file_path", help="manually specify the \"My Clippings.txt\" file path (defaults to the \"My Clippings.txt\" file path on a connected Kindle device)")
    par.add_argument("-out", "--output", metavar="output_folder", help="manually specify the output folder for the HTML file with converted clippings (defaults to desktop)")
    par.add_argument("-nopr", "--no_preview", action="store_true", help="do not automatically open the HTML file with converted clippings")
    par.add_argument("-ns", "--no_style", action ="store_true", help="do not add CSS styling to the HTML file with converted clippings")
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