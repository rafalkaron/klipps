"""
Convert files to different formats.
"""

import mistune
import re
import datetime

__author__ = 'Rafał Karoń <rafalkaron@gmail.com>'

def clipps_to_md(md_str):
    """Applies Markdown syntax to a raw string from a \"Kindle Clippings.txt file\""""
    timestamp = datetime.datetime.now()
    heading = "# Kindle Clippings\n\n---\n"
    md_str = re.sub("==========", "\n---\n", md_str)
    md_str = re.sub(r"- Your Highlight at location.* \| ", "", md_str)

    for book_title in re.findall(r"^.*. \(.*\)$", md_str, re.MULTILINE):    # This does not work. Dunny why.
        new_book_title = f"## {book_title}  "
        md_str = re.sub(book_title, new_book_title, md_str)
    
    for match in re.findall(r"^Added on .*,*. \d.* \d\d:\d\d:\d\d$", md_str, re.MULTILINE):
        new_match = f"*{match}*"
        md_str = re.sub(match, new_match, md_str)
    
    for quote in re.findall(r"^.*\n\n---$", md_str, re.MULTILINE): # Groups raise an error r"(^(?!\#).*\n\n)(---$)"
        new_quote = f"> {quote}"
        md_str = re.sub(quote, new_quote, md_str)

    footer = f"Generated on {timestamp.strftime('%d %B, %Y')} at {timestamp.strftime('%-I:%-M %p')} with [Klipps](https://github.com/rafalkaron/Klipps/releases)."
    md_str = "\n".join((heading, md_str, footer))
    return md_str

def md_str_to_md(md_str, dir):
    """Saves a Markdown string to a md file"""          # The out name should match the input file. Probably need to create a class.
    out = f"{dir}/My Clippings.md"
    with open(out, "w") as md_file:
        md_file.write(md_str)
        return out

def md_str_to_html_str(md_str):
    """Exports a Markdown string to a HTML5 file"""
    html_str = mistune.markdown(md_str)
    return html_str

def style_html_str(html_str):
    """Embeds CSS styling in a HTML5 file"""
    # Adds missing HTML5 elements
    html_declaration = "<!DOCTYPE html>"
    html_tag_open = "<html>"
    html_tag_close = "</html>"
    # Update favicons with sth more civilised
    head = "<head>\n<title>Kindle Clippings</title>\n<link href='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAC4HpUWHRSYXcgcHJvZmlsZSB0eXBlIGV4aWYAAHja7ZdBkuQoDEX3nKKPgCSE4DhgIGJuMMfvDyadma7ujuiKWcwiTdjYKvwl/sNUlev//jPcDxyUhV1QSzHH6HGEHDIX3CR/HmdPPqzrfvCPm7e4u37ACAl6OR9j3+ML4vp8wcKO1/e4s2PrpC1El/A6ZGae920XuYWEzzjtZ5f3CyW+TGeffGzZLX5/DgYzmkIPHnEXEn9ez0xyngVnwJWF+REJousav/rn/KuHNwOvu5t//lGZPO04hR7Tijefdpz0FpcrDb9VRHxl5teKTK4UX/wbo6Ux+jm7EqKDXXFP6jGVdYeBFXbKei2iGU7Fva2W0ZIv/gC1hqlW5yseMjG8HhSoUaFBffUHHSgxcGdDz3ywrFgS48wH7CcYj0aDzUmWJglUDpAThPmqhVbePPMhWULmRhjJBDGaNF+buwe+296ExpjLnMinyyvUxXPJooxJbl4xCkBobE91+Uvu7Pz9mGAFBHXZnDDB4uspUZWea0sWZ/HqMDT483sha1sAFiG3ohgSEPCRRCmSN2Yjgo8JfAoqZwlcQYDUKTdUyUEkAk7imRvvGK2xrHyGsb2sDySKAU2WAlghaIj43hKWUHEqGlQ1qmnSrCVKDFFjjBbnPlVMLJhaNLNk2UqSFJKmmCyllFPJnAXbmLocs+WUcy4FSUso0CoYXxCoXKWGqjVWq6nmWg4snyMcesTDjnTkozRu0rAFuBabtdRyK506llIPXXvs1lPPvQystSEjDB1x2Egjj3JR21Tfqd3J/ZkabWq8QM1x9qSGsNlDguZ2opMZiHEgELdJAAuaJzOfKASe5CYzn1mciDKq1Amn0SQGgqET66CL3ZPcb7k5uPu33PhX5NxE91+QcxPdC7mv3H5BrZW13coCNL9CeIodUvD5YUBPhVOZv5e+1bvvvvgR+gh9hD5CH6GP0Efo/yk08MdDxr9TPwGC3JHgUNi9JgAAAYVpQ0NQSUNDIFBST0ZJTEUAAHicfZE9SMNAHMVf00pFKoIWEXHIUJ0siIo4ahWKUCHUCq06mFzaWmjSkKS4OAquBQc/FqsOLs66OrgKguAHiJOjk6KLlPi/pNAixoPjfry797h7Bwj1MtOs0Big6baZTibEbG5FDL8ihH70Io6wzCxjVpJS8B1f9wjw9S7Os/zP/Tm61bzFgIBIPMMM0yZeJ57atA3O+8RRtiGrxOfEoyZdkPiR64rHb5yLLgs8M2pm0nPEUWKx2MZKG7MNUyOeJI6pmk75QtZjlfMWZ61cZc178hdG8vryEtdpDiGJBSxCgggFVZRQhk19laCTYiFN+wkf/6Drl8ilkKsERo55VKBBdv3gf/C7W6swMe4lRRJAx4vjfAwD4V2gUXOc72PHaZwAwWfgSm/5K3Vg+pP0WkuLHQE928DFdUtT9oDLHWDgyZBN2ZWCNIVCAXg/o2/KAX23QNeq11tzH6cPQIa6St0AB4fASJGy13ze3dne279nmv39AFpFcp0odYUNAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAC4jAAAuIwF4pT92AAAAB3RJTUUH5AQWEi0uIq19iQAAAJJJREFUOMvN0yEOAjEQBdC3hKxGojkEhkNgcCRYFIKTIFDoFXAQ5B6CoJCYFajFDCQ0aQjB9Cff/P7+6UymlIYFOvQZduF5o0oCGkywzxTY4ILlSxgmhgGuOGUC5uH5uPAXyguoimthFvwpoMYKLc7BNrT624uOsXGPWKppsAmtD092aDvcccAtORtjjRG25fy+JzIyHM2D1RGSAAAAAElFTkSuQmCC'rel='icon' type='image/png'/></head>"
    body_open = "<body>"
    body_close = "</body>"
    html_str = "\n".join((html_declaration, html_tag_open, head, body_open, html_str, body_close, html_tag_close))

    html_str = re.sub("<body>", "<body style=\"width:60%; background-color: #F7F4F3; margin:auto; font-family: \'Helvetica Neue\', Helvetica, Arial, sans-serif;\">", html_str)
    html_str = re.sub("<h1>", "<h1 style=\"color:#5B2333\">", html_str)
    html_str = re.sub("<hr>", "<hr style=\"background-color:#564D4A\">", html_str)
    html_str = re.sub("<h2>", "<h2 style=\"color:BA1B1D\">", html_str)
    return html_str

def save_str_as_file(str, filepath):
    """Save a string as a file"""
    out = filepath
    with open(out, "w") as file:
        file.write(str)
    return out