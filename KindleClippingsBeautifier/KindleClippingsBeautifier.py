# coding: utf-8
__version__ = "0.2"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

"""
    Kindle Clippings Beautifier (Codename: Unchanging Tick)
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
    - Enumerate output files
    - Default settings
    - Customization (Name, e.g. Fred's Clippings)
"""
#Modules
import os
import datetime
import re       #regular expression
#Global Variables
_timestamp = datetime.datetime.now()
_timestamp_formatted = str(_timestamp.strftime("%d_%m_%y-%H-%M-%S"))
_script_filepath = os.path.abspath(__file__)                                            #gets this script filepath
_script_filename = os.path.basename(__file__)                                           #gets this script filename
_script_directory = _script_filepath.replace(_script_filename, "").replace("\\", "/")   #prints the script directory w/o its filename

#Functions
def intro():
    print("Beautify your Kindle clippings by exporting them to a Markdown file.")

def main_menu():
    _output_type = input("Select the output format for your Kindle clippings by entering one of the following:\n[md] to convert your Kindle clippings to Markdown\n[pdf] to convert your Kindle clippings to PDF\n[html] to convert your Kindle clippings to a website format (HTML5)\n")
    if _output_type == "md" or _output_type == "MD" or _output_type == "[md]" or _output_type == "[MD]":
        kindle_to_md()
    elif _output_type == "pdf" or _output_type == "PDF" or _output_type == "[pdf]" or _output_type == "[PDF]":
        kindle_to_pdf()
    elif _output_type == "html" or _output_type == "HTML" or _output_type == "[html]" or _output_type == "[HTML]":
        kindle_to_html5()
    else:
        print("Try answering the following question again.")
        main_menu()

def kindle_to_md():
    global _kindle_to_md_called
    _kindle_to_md_called = True
    
    out_folder()
    global _out_md
    _out_md = open(str(_out_folder) + "/" + "My Clippings" + ".md", "w+t", encoding="utf-8")
    _clippings_filepath = input("Enter a full path to the \"Kindle Clippings.txt\" file: ")
    _clippings_file = open(_clippings_filepath, "rt", encoding ="utf-8")

    output_title_header()

    with _clippings_file as file:
        filedata = file.read()
    filedata = filedata.replace("==========", "") #.replace can be stacked
    with _out_md as file:
        file.write(filedata)

    file.close
    _out_md.close
_kindle_to_md_called = False

def kindle_to_pdf():
    global _kindle_to_pdf_called
    _kindle_to_pdf_called = True
    kindle_to_md()
    #os.system("cd "+ str(_script_directory) + "DITA-OT/bin && dita -i " + "\"../../out/My Clippings.md\"" + " -f pdf2")     #improve path handling

_kindle_to_pdf_called = False

def kindle_to_html5():
    global _kindle_to_html5_called
    _kindle_to_html5_called = True
_kindle_to_html5_called = False

def output_title_header():
    _out_md.write("# My Kindle Clippings" + "\n" + " _Generated on " + str(_timestamp.strftime("%x")) + " at " + str(_timestamp.strftime("%X")) + "_\n\n")

def out_folder():
    global _out_folder
    _out_folder = ("out")
    if not os.path.exists(_out_folder):
        os.mkdir(_out_folder)

def src_folder():
    global _src_folder
    _src_folder = ("src")
    if not os.path.exists(_src_folder):
        os.mkdir(_src_folder)

def summary():
    if _kindle_to_md_called == True and _kindle_to_pdf_called == False:             #improve this by adding HTML5 option
        print("Your Kindle clippings were converted to Markdown.")
    elif _kindle_to_pdf_called == True:
        print("Your Kindle clippings were converted to PDF.")
    elif _kindle_to_html5_called == True:
        print("Your Kindle clippings were converted to a website format (HTML5).")

#Invocations
intro()
#main_menu()
#kindle_to_md()
kindle_to_pdf()
summary()
exit()