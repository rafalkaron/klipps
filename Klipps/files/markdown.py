"""
Perform Markdown-related tasks.
"""

import mistune
import re

__author__ = 'Rafał Karoń <rafalkaron@gmail.com>'

def clipps_to_md(clippings_file):
    """Applies Markdown syntax to a raw \"Kindle Clippings.txt file\""""    
    print(clippings_file)

def md_to_html(md_file):
    """Exports Markdown to HTML5"""
    with open(re.sub(r"(.md|.markdown)", r".html", md_file, flags=re.IGNORECASE), "w") as html_file:
        markdown_file = open(md_file)
        md_file_str = markdown_file.read()
        markdown_file.close()
        html_file.write(mistune.markdown(md_file_str))