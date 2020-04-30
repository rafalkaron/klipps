# coding: utf-8
import os
import sys

__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

def clipps_filepath():
    """Return the \"My Clippings.txt\" file path"""

    if os.name == "nt":
        volumes = ["A", "D", "E", "F", "G", "H"]
        for volume in volumes:
            print(volume)
            clipps_path = volume + r":\documents\My Clippings.txt"
            clipps_exist = os.path.isfile(clipps_path)
            if clipps_exist:
                return clipps_path
            if not clipps_exist:
                continue
        
    if os.name == "posix":
        clipps_path = r"/Volumes/Kindle/documents/My Clippings.txt"
        clipps_exist = os.path.isfile(clipps_path)
        if clipps_exist == False:
            enter_clipps_filepath()
        return clipps_path

def enter_clipps_filepath():
    print("Klipps cannot locate your Kindle Clippings file!' The \"My Clippings.txt\" file is saved in the \"Documents\" directory on your Kindle device.\nNote: Ensure that your Kindle is connected and discovered by the computer. Some third-party USB cables may prevent your computer from correctly discovering your Kindle device.")
    clipps_path = input("\nProvide the file path to the \"My Clippings.txt\" file manually or press [Enter] to exit Klipps: ")
    filepath_exist = os.path.isfile(clipps_path)
    if filepath_exist == False:
        print("")
        sys.exit(0)    
    return clipps_path

def read_file(filepath):
    """Return a string with file contents."""
    with open(filepath, mode='rt', encoding='utf-8') as f:
        return f.read()