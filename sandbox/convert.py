"""
Convert files to different formats.
"""

import mistune
import re

__author__ = 'Rafał Karoń <rafalkaron@gmail.com>'

def md_str_to_html(md_str, filepath):
    """Exports a Markdown string to a HTML5 file"""
    out = filepath
    with open(out, "w") as html_file:
        html_str = mistune.markdown(md_str)
        html_file.write(html_str)
    return out

def md_to_html(file):                                                                               # The most universal here
    """Exports a Markdown file to a HTML5 file"""
    with open(re.sub(r"(.md|.markdown)", r".html", file, flags=re.IGNORECASE), "w") as html_file:
        with open(file, "rt") as md_file:
            md_file_str = md_file.read()
            html_file.write(mistune.markdown(md_file_str))