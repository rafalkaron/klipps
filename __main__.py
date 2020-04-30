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
    
    if os.name == "nt":
        try:
            clipps_path = r"D:\documents\My Clippings.txt"
            clipps_exist = os.path.isfile(clipps_path)
            print("tried!")
        except:
            clipps_path = r"E:\documents\My Clippings.txt"
            clipps_exist = os.path.isfile(clipps_path)
        else:
            print("Klipps cannot locate your Kindle Clippings file!' The \"My Clippings.txt\" file is saved in the \"Documents\" directory on your Kindle device.\nNote: Ensure that your Kindle is connected and discovered by the computer. Some third-party USB cables may prevent your computer from correctly discovering your Kindle device.")
        finally:
            if clipps_exist == False:
                clipps_path = input("\nProvide the file path to the \"My Clippings.txt\" file manually or press [Enter] to exit Klipps: ")
                filepath_exist = os.path.isfile(clipps_path)
                if filepath_exist == False:
                    print("")
                    sys.exit(0)

    if os.name == "posix":
        clipps_path = r"/Volumes/Kindle/documents/My Clippings.txt"
        clipps_exist = os.path.isfile(clipps_path)

    pb(10)
    html_str = clipps_str_to_html_str(read_file(clipps_path))
    pb(25)
    html_path = os.path.normpath(os.path.expanduser("~/Desktop")) + f"/{os.path.basename(clipps_path)}".replace(".txt", ".html")
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