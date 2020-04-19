"""
Perform Markdown-related tasks.
"""

import mistune
import re

__author__ = 'Rafał Karoń <rafalkaron@gmail.com>'

def clipps_to_md(file):
    """Applies Markdown syntax to a raw \"Kindle Clippings.txt file\""""    
    # Mark up with markdown syntax here
    
    markdown = file
    return markdown
    
def str_md_to_html(md_str, dir):
    """Exports a Markdown string to a HTML5 file"""
    out = f"{dir}/My Clippings.html"
    with open(out, "w") as html_file:
        html_file.write(mistune.markdown(md_str))
        return out

def save_to_md(str):
    """Saves a string to a Markdown file"""

def md_to_html(file):
    """Exports a Markdown file to a HTML5 file"""
    with open(re.sub(r"(.md|.markdown)", r".html", file, flags=re.IGNORECASE), "w") as html_file:
        md_file = open(file)
        md_file_str = md_file.read()
        md_file.close()
        html_file.write(mistune.markdown(md_file_str))