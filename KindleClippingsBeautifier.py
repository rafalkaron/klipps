# coding: utf-8
__version__ = "0.3"
__author__ = "Rafał Karoń <rafalkaron@gmail.com.com>"

"""
    Kindle Clippings Beautifier (Codename: Sequential Tick)
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
    - Default settings
    - Customization (Name, e.g. Fred's Clippings)
"""
#Modules
import os, datetime, re

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

def feed():
    global _clippings_filepath
    _clippings_filepath = input("Enter a full path to the \"Kindle Clippings.txt\" file: ")

def kindle_to_md():
    #Checks if the function was called
    global _kindle_to_md_called
    _kindle_to_md_called = True
    #Folders and Files
    feed()
    tmp()
    out()
    #Document Manipulation
    _header = str("# My Kindle Clippings" + "\n" + " _Generated on " + str(_timestamp.strftime("%x")) + " at " + str(_timestamp.strftime("%X")) + "_\n\n")    

    with open(_clippings_filepath, "rt", encoding ="utf-8") as _in_file:
        _clippings_filepath_lines = _in_file.readlines()
        for line in _clippings_filepath_lines:
            if line.startswith("=========="):
                line = line + "## "
            _tmp_md.write(line)

    with open(_clippings_filepath, "rt", encoding ="utf-8") as _in_file:
        _sr = _in_file.read()                                                            #STR makes this file to load onto the memory
        _sr = re.sub("==========", "", _sr)                                         #Removes underlines //h2in a new line? #remove clippings file @begginign? Inswert newline below. Alternative - check for - Your gihglight and place ## two lines below
        _sr = re.sub(r"- Your Highlight at location.* \| ", "", _sr)                #Removes redundant highlight location

    with open (_out_md_filepath, "w+t", encoding="utf-8") as _out_file:
        _out_file.write(_header)
        _out_file.write(_sr)

_kindle_to_md_called = False

def kindle_to_pdf():
    global _kindle_to_pdf_called
    _kindle_to_pdf_called = True
    kindle_to_md()
    os.system("cd "+ str(_script_directory) + "DITA-OT/bin && dita -i " + "\"../../out/My Clippings.md\"" + " -f pdf2")     #improve path handling #think about prince
_kindle_to_pdf_called = False

def kindle_to_html5():
    global _kindle_to_html5_called
    _kindle_to_html5_called = True
_kindle_to_html5_called = False

def tmp():
    _tmp_folder = (str(_script_directory) + "tmp")
    if not os.path.exists(_tmp_folder):
        os.mkdir(_tmp_folder)    
    global _tmp_md
    _tmp_md = open(str(_tmp_folder) + "/tmp.md", "w+t", encoding="utf-8")
    global _tmp_md_filepath
    _tmp_md_filepath = str((_tmp_folder) + "/tmp.md")

def out():
    _out_folder = (str(_script_directory) + "out")
    if not os.path.exists(_out_folder):
        os.mkdir(_out_folder)
    i = 0
    if _kindle_to_md_called == True:
        while os.path.exists(str(_out_folder) + "/" + "My Clippings (%s)" %i + ".md"):
            i += 1
        global _out_md
        _out_md = open(str(_out_folder) + "/" + "My Clippings (%s)" %i + ".md", "w+t", encoding="utf-8")
        global _out_md_filepath
        _out_md_filepath = str((_out_folder) + "/" + "My Clippings (%s)" %i + ".md")

def src_folder():
    global _src_folder
    _src_folder = (str(_script_directory) + "src")
    if not os.path.exists(_src_folder):
        os.mkdir(_src_folder)

def summary():
    if _kindle_to_md_called == True and _kindle_to_pdf_called == False and _kindle_to_html5_called == False:
        print("Your Kindle clippings were converted to Markdown.")
    elif _kindle_to_pdf_called == True:
        print("Your Kindle clippings were converted to PDF.")
    elif _kindle_to_html5_called == True:
        print("Your Kindle clippings were converted to a website format (HTML5).")

#Invocations
intro()
#main_menu()
kindle_to_md()
#kindle_to_pdf() ##use prince instead of dita-ot?
summary()
exit()