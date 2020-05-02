# coding: utf-8
import os
import sys

__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

def get_clipps_filepath():
    """Automatically return the \"My Clippings.txt\" file path.
    As a fallback, call the enter_clipps_filepath() function to prompt the user to provide the \"My Clippings.txt\" file path."""

    if os.name == "nt":
        drive_letters = ["D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "manual"]
        for drive_letter in drive_letters:
            clipps_path = drive_letter + r":\documents\My Clippings.txt"
            clipps_exist = os.path.isfile(clipps_path)
            if clipps_exist:
                return clipps_path
            if drive_letter == "manual":
                enter_clipps_filepath()
            if not clipps_exist:
                continue
        
    if os.name == "posix":
        clipps_path = r"/Volumes/Kindle/documents/My Clippings.txt"
        clipps_exist = os.path.isfile(clipps_path)
        if clipps_exist:
            return clipps_path
        if not clipps_exist:
            clipps_path = enter_clipps_filepath()
            return clipps_path
    
def enter_clipps_filepath():
    """Enter the \"My Clippings.txt\" file path.
    This function is called as a fallback of the "get_clipps_filepath()" function."""
    clipps_path = input("""
Klipps cannot locate the \"My Clippings.txt\" file that is usually in the \"documents\" directory on your Kindle.
    
Before running Klipps again, ensure that:
  * You highlighted some quotes while reading on your Kindle
  * Your Kindle is connected to and discovered by your computer
    NOTE: Some third-party USB cables may prevent your computer from correctly discovering your Kindle.

You can manually enter the \"My Clippings.txt\" file path or press [Enter] to exit Klipps: """).replace("\"", "").replace("\'","")
    filepath_exist = os.path.isfile(clipps_path)
    if filepath_exist == False:
        sys.exit(0)    
    return clipps_path

def read_file(filepath):
    """Return a string with file contents."""
    with open(filepath, mode='rt', encoding='utf-8') as f:
        return f.read()