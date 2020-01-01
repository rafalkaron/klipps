# coding: utf-8
__version__ = "0.1"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

"""
    Kindle Clippings Beautifier (Codename: Undefined Zit)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Beautify your Kindle clippings by exporting them to a desired format.
    
    Upcoming features:
    - Automatically detect the "My Clippoings.txt" file @ connected Kindle
    - Send converted files to an email
    - Convert to Markdown
    - Convert to PDF by using DITA-OT
    - Convert to HTML5 by using DITA-OT
    - CLI
    - GUI
    - EXE
"""
#Modules
import os
import datetime

#Global Variables
_timestamp = datetime.datetime.now()
_timestamp_formatted = str(_timestamp.strftime("%d_%m_%y-%H-%M-%S"))

print(_timestamp_formatted)

#Functions
def intro():
    print("Beautify your Kindle clippings by exporting them to a Markdown file.")

def main_menu():
    _query = input("Enter one of the following:\n[md]")
    if _query == "md" or _query == "MD" or _query == "[md]" or _query == "[MD]":
        kindle_to_md()
    else:
        print("Try answering the following question again.")
        main_menu()

def kindle_to_md():
    global _kindle_to_md_called
    _kindle_to_md_called = True
    _file_location = input("Enter a full path to the \"Kindle Clippings.txt\" file: ")
    open(_file_location)
    #remove "Your Highlight..."
_kindle_to_md_called = False

def out_folder():
    global _out_folder
    _out_folder = ("out") #add Path if sth goes wrong and from pathlib import Path
    if not os.path.exists(_out_folder):
        os.mkdir(_out_folder)

def src_folder():
    global _src_folder
    _src_folder = ("src") #add Path if sth goes wrong and from pathlib import Path
    if not os.path.exists(_src_folder):
        os.mkdir(_src_folder)

def summary():
    if _kindle_to_md_called == True:
        print("Your Kindle clippings were converted to Markdown.")

#Invocations
intro()
main_menu()
summary()
exit()