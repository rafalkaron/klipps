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

def save_to_md(str):
    """Saves a string to a Markdown file"""
    
def str_md_to_html(md_str, dir):
    """Exports a markdown string to a HTML5 file"""
    with open(f"{dir}/converted_markdown_string.html", "w") as html_file:
        html_file.write(mistune.markdown(md_str))
        return f"{dir}/converted_markdown_string.html"

def md_to_html(file):
    """Exports Markdown to HTML5"""
    with open(re.sub(r"(.md|.markdown)", r".html", file, flags=re.IGNORECASE), "w") as html_file:
        md_file = open(file)
        md_file_str = md_file.read()
        md_file.close()
        html_file.write(mistune.markdown(md_file_str))