"""
Perform Markdown-related tasks.
"""

import mistune
import re

__author__ = 'Rafał Karoń <rafalkaron@gmail.com>'

def clipps_to_md(md_str):
    """Applies Markdown syntax to a raw string from a \"Kindle Clippings.txt file\""""
    heading = "# My Kindle Clippings"
    md_str = re.sub("==========", "", md_str)
    md_str = re.sub(r"- Your Highlight at location.* \| ", "", md_str)
    footer = "--- \n\n **Generated  with [Klipps](https://github.com/rafalkaron/Klipps/releases)**."
    md_str = "\n".join((heading, md_str, footer))
    return md_str
    
def md_str_to_html(md_str, dir):                        # Add a function that embeds CSS in html to style the output
    """Exports a Markdown string to a HTML5 file"""
    out = f"{dir}/My Clippings.html"                    # The out name should match the input file. Probably need to create a class.
    with open(out, "w") as html_file:
        html_file.write(mistune.markdown(md_str))
        return out

def md_str_to_html_css(md_str, dir):                        # Add a function that embeds CSS in html to style the output
    """Exports a Markdown string to a HTML5 file"""
    out = f"{dir}/My Clippings.html"                    # The out name should match the input file. Probably need to create a class.
    with open(out, "w") as html_file:
        html_str = mistune.markdown(md_str)
        html_str = re.sub("<h1>", "<h1 style=\"color:red\">", html_str)
        html_file.write(html_str)
        return out

def md_str_to_md(md_str, dir):
    """Saves a Markdown string to a md file"""          # The out name should match the input file. Probably need to create a class.
    out = f"{dir}/My Clippings.md"
    with open(out, "w") as md_file:
        md_file.write(md_str)
        return out

def md_to_html(file):
    """Exports a Markdown file to a HTML5 file"""
    with open(re.sub(r"(.md|.markdown)", r".html", file, flags=re.IGNORECASE), "w") as html_file:
        with open(file, "rt") as md_file:
            md_file_str = md_file.read()
            html_file.write(mistune.markdown(md_file_str))