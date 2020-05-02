# coding: utf-8
"""
Connect your Kindle to the computer, run Klipps, and automatically export your Kindle clippings to an HTML file on your desktop.
"""

import sys
import re
import os
import argparse
import time
from Klipps import (get_clipps_filepath,
                    read_file,
                    progressbar as pb,
                    clipps_str_to_html_str,
                    style_html_str,
                    save_str_as_file,
                    open_file,
                    exit_prompt)

__version__ = "0.8"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

def main():
    print(f"Let's export your Kindle clippings with Klipps {__version__}!")
    par = argparse.ArgumentParser(description="Export clippings from a Kindle device to an HTML file on your desktop.", formatter_class=argparse.RawTextHelpFormatter)
    par.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    par.add_argument("-in", "--input", metavar="clippings_file_path", help="manually specify the \"My Clippings.txt\" file path (defaults to the \"My Clippings.txt\" file path on a connected Kindle device)")
    par.add_argument("-out", "--output", metavar="output_folder", help="manually specify the output folder for the HTML file with converted clippings (defaults to desktop)")
    par.add_argument("-nopr", "--no_preview", action="store_true", help="do not automatically open the HTML file with converted clippings")
    par.add_argument("-ns", "--no_style", action ="store_true", help="do not add CSS styling to the HTML file with converted clippings")
    par.add_argument("-ex", "--exit", action ="store_true", help="exits without a prompt (defaults to prompt on exit)")
    args = par.parse_args()
    if not args.input:
        in_path = get_clipps_filepath()
    if args.input:
        in_path = args.input
    print(f"Klipps will export the following file \"{in_path}\"")
    if not args.output:
        out_path = f"{os.path.normpath(os.path.expanduser('~/Desktop'))}/{os.path.basename(in_path)}".replace(".txt", ".html").replace("\\", "/").replace("//", "/")
    if args.output:
        out_path = f"{args.output}/{os.path.basename(in_path)}".replace(".txt", ".html").replace("\\", "/").replace("//", "/")
    pb(10)
    start_time = time.time()
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
        elapsed_time = time.time() - start_time # does not work without Kindle attached.
        pb(100)
        print(f"Klipss succesfully exported Kindle clippings to \"{out_path}\" in {int(elapsed_time)} seconds.")
    except(PermissionError):
        pb(100)
        print(f"Klipps cannot save the converted Kindle clippings as \"{out_path}\" because you lack permissions.\nTry running Klipps again as an administrator or selecting another directory.")
    if not args.exit:
        exit_prompt("\nTo exit Klipps, press [Enter]")

if __name__ == "__main__":
    main()