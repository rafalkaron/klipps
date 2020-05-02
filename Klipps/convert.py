# coding: utf-8
import re
import datetime

__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

def clipps_str_to_html_str(clipps_str):
    """Return a string that contains the converted \"Kindle Clippings.txt file\" to HTML."""
    # ADD ELEMENTS
    pre_elements = "<!DOCTYPE html>\n<html>\n<head></head>\n<body>"
    heading = "<h1>Kindle Clippings</h1>\n<h2>"
    footer = f"<div class=\"footer\">Generated on {datetime.datetime.now().strftime('%B %d, %Y')} at {datetime.datetime.now().strftime('%I:%M %p')} with <a href=\"https://github.com/rafalkaron/Klipps/releases\">Klipps</a></div>"
    post_elements = "</body>\n</html>"
    html_str = "\n".join((pre_elements, heading, clipps_str, footer, post_elements))
    # SEARCH AND REPLACE
    html_str = re.sub(r"\n\n", "\n", html_str)  # Removes empty lines
    html_str = re.sub(r"==========", "<div class=\"entry\">\n<h2>", html_str)   # Replaces Kindle entryies markup with the "entry" class and opens headers 2
    html_str = re.sub(r"- .* \| ", "###timestamp### ", html_str)   # Removes redundant information from timestamps and adds a tag that is used to optimize RE in the next lines
    for added_on in re.findall(r"^###timestamp### .*", html_str, re.MULTILINE):    # Shortens and wraps timestamps || MAKE THIS GENERIC FOR OTHER LANGUAGES
        added_on_new = re.sub(r"###timestamp###", "", added_on) # Removes the ###timestamp### tag
        added_on_new = re.sub(r":\d\d$", "", added_on_new, re.MULTILINE)    # [Optional] Removes seconds in 24h timestamps
        added_on_new = re.sub(r":\d\d PM$", " PM", added_on_new, re.MULTILINE)    # [Optional] Removes seconds in 12h PM timestamps
        added_on_new = re.sub(r":\d\d AM$", " AM", added_on_new, re.MULTILINE)    # [Optional] Removes seconds in 12h AM timestamps
        added_on_new = re.sub(r"^ Added on ", "", added_on_new)    # [Optional] Removes the "Added on" timestamp text
        added_on_new = f"<div class=\"timestamp\">{added_on_new}</div>\n<blockquote>"   # Wraps timestamps in timestamp divs and opens a blockquote
        html_str = re.sub(added_on, added_on_new, html_str)
    html_str = re.sub(r"<div class=\"timestamp\">", "</h2>\n<div class=\"timestamp\">", html_str)   # Closes headers 2 before timestamps
    html_str = re.sub(r"<div class=\"entry\">\n<h2>\n<div class=\"footer\">", "</blockquote>\n</div>\n<div class=\"footer\">", html_str)    # Removes redundant entry divs and headers 2 before the footer
    html_str = re.sub("<div class=\"entry\">\n<h2>", "</blockquote>\n</div>\n<div class=\"entry\">\n<h2>", html_str)    # Closes blockquote and entry div before opening anothe entry div
    html_str = re.sub(r"</h1>\n<h2>", "</h1>\n<div class=\"entry\">\n<h2>", html_str)   # Opens the first element div after
    return html_str

def style_html_str(html_str):
    """Return a string that contains the converted to HTML \"Kindle Clippings.txt file\" with embedded CSS and an encoded favicon."""
    # ADDS ROW DIV - need to add it every second instance
    #html_str = re.sub("<div class=\"entry\">", "<div class=\"row\">\n<div class=\"entry\">", html_str)
    #html_str = re.sub("</blockquote>\n</div>", "</blockquote>\n</div>\n</div>", html_str)
    # ADDS A TITLE, FAVICON, AND CSS
    html_str = re.sub("<head></head>", """<head>
<title>Kindle Clippings</title>
<link href='data:image/png;base64,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'rel='icon' type='image/png'/>
<style>
body{
width:90%; 
font-size: 100%;
background-color: #F2E9E4; 
margin:auto; 
font-family: \'Helvetica Neue\', Helvetica, Arial, sans-serif;
}
.entry{
    border: 2px solid #22223B;
    border-radius: 10px;
    margin: 2px; 
    width: 48%; 
    float: left;
}

h1{
    font-size:7rem;
    text-align: center;
    margin-top: 0.2em;
    margin-bottom: 0.4em;
    margin: 1em, 0em, 1em, 0em;
    font-weight: lighter;
    color: #22223B;
}

h2{
    color: #4A4E69
}

.timestamp{
    color: #9A8C98;
}

blockquote{
    background-color: #C9ADA7; padding: 1em; margin: 0em;
    border-radius: 0px 0px 10px 10px;
    text-align: justify;
}

.footer{
    position: fixed;
    bottom: 0;
}
</style>
</head> """, html_str)
    return html_str