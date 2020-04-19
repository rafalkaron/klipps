"""
Perform Markdown-related tasks.
"""

import mistune
import re

__author__ = 'Rafał Karoń <rafalkaron@gmail.com>'

def clipps_to_md(file):
    """Applies Markdown syntax to a raw \"Kindle Clippings.txt file\""""    
    print(file)

def md_to_html(file):
    """Exports Markdown to HTML5"""
    with open(re.sub(r"(.md|.markdown)", r".html", file, flags=re.IGNORECASE), "w") as html_file:
        md_file = open(file)
        md_file_str = md_file.read()
        md_file.close()
        html_file.write(mistune.markdown(md_file_str))