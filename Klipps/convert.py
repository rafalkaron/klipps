"""
Convert files to different formats.
"""

import mistune
import re
import datetime
from Klipps import read_file_lines

__author__ = 'Rafał Karoń <rafalkaron@gmail.com>'    

def clipps_str_to_md_str(clipps_str):
    """Applies Markdown syntax to a raw string from a \"Kindle Clippings.txt file\""""
    """
    entries_list = re.findall(r"==========([^;]*)==========", clipps_str, re.MULTILINE) #try with groups again
    print(entries_list[2])
    """
    md_str = re.sub("==========", "", clipps_str)
    md_str = re.sub(r"- Your Highlight at location.* \| ", "", md_str)

    for added_on in re.findall(r"^Added on .*,*. \d.* \d\d:\d\d:\d\d$", md_str, re.MULTILINE):
        added_on_short = re.sub(r"^Added on .*, ", "", added_on, re.MULTILINE)
        added_on_shorter = re.sub(r":\d\d$", "", added_on_short, re.MULTILINE)
        added_on_new = f"`{added_on_shorter}`"
        md_str = re.sub(added_on, added_on_new, md_str)
    
    for quote in re.findall(r"^\n.*\n\n", md_str, re.MULTILINE): # Groups raise an error r"(^(?!\#).*\n\n)(---$)"
        new_quote = f"> {quote}"
        md_str = re.sub(quote, new_quote, md_str)

    """
    tit_regex = re.compile(r"^.* +\(.*\)$", re.MULTILINE)   #if the whole line matches r"^.* +\(.*\)$", it replaces all lines with the last match. If not the whole line matches, multiplies the tit new string +\(.*\)$"
    tits = re.findall(tit_regex, md_str)
    for tit in tits:
        tit_new = f"## {tit}"
        md_str = re.sub(tit_regex, tit_new, md_str)
    """
    """
    cite_regex = re.compile(r"\n\n.*\n\n", re.MULTILINE)
    cites = re.findall(cite_regex, md_str)
    for cite in cites:
        cite_new = f"> {cite}"
        md_str = re.sub(cite, cite_new, md_str)
    """
    heading = "# Kindle Clippings"
    footer = f"Generated on {datetime.datetime.now().strftime('%B %d, %Y')} at {datetime.datetime.now().strftime('%-I:%-M %p')} with [Klipps](https://github.com/rafalkaron/Klipps/releases)."
    md_str = "\n".join((heading, md_str, footer))
    return md_str

def md_str_to_md(md_str, dir):
    """Saves a Markdown string to a md file"""          # The out name should match the input file. Probably need to create a class.
    out = f"{dir}/My Clippings.md"
    with open(out, "w") as md_file:
        md_file.write(md_str)
        return out

def md_str_to_html_str(md_str):
    """Exports a Markdown string to HTML string."""
    html_str = mistune.markdown(md_str)
    return html_str

def style_html_str(html_str):
    """Embeds CSS styling in a HTML5 file and adds missing HTML5 elements."""
    html_declaration = "<!DOCTYPE html>"
    html_tag_open = "<html>"
    html_tag_close = "</html>"
    head = "<head>\n<title>Kindle Clippings</title>\n<link href='data:image/png;base64,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'rel='icon' type='image/png'/></head>"
    body_open = "<body>"
    body_close = "</body>"
    html_str = "\n".join((html_declaration, html_tag_open, head, body_open, html_str, body_close, html_tag_close))
    html_str = re.sub("<body>", "<body style=\"width:60%; background-color: #F7F4F3; margin:auto; font-family: \'Helvetica Neue\', Helvetica, Arial, sans-serif;\">", html_str)
    html_str = re.sub("<h1>", "<h1 style=\"margin-top:10px;margin-bottom:15px;font-weight:bolder; font-size:400%; color:#5B2333; border-bottom: 8px solid #564D4A;\">", html_str)
    html_str = re.sub("<hr>", "<hr style=\"background-color:#564D4A\">", html_str)
    html_str = re.sub("<code>", "<div class=\"timestamp\" style=\"margin-top:0px; margin-bottom:0px; color:#564D4A; font-size:80%\">", html_str)
    html_str = re.sub("</code>", "</div>", html_str)
    html_str = re.sub("<h2>", "<h2 style=\"margin-top:10px; margin-bottom:0px; font-size:180%; font-weight:normal\">", html_str)
    html_str = re.sub("<blockquote>", "<div class=\"cite\" style=\"text-align:justify;border-bottom: 2px solid #564D4A; font-size:90%; margin-bottom:0px; margin-top:0px;\">", html_str)
    html_str = re.sub("</blockquote>", "</div>", html_str)
    html_str = re.sub("<a href=", "<a target='blank' style='text-decoration: none; color:#5B2333; font-weight:bold'href=", html_str)
    return html_str

def save_str_as_file(str, filepath):
    """Save a string as a file"""
    out = filepath
    with open(out, "w") as file:
        file.write(str)
    return out
