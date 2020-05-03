# coding: utf-8
import re
import datetime
from .feed import read_file

__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

def clipps_str_to_html_str(clipps_str):
    """Return a string that contains the converted \"Kindle Clippings.txt file\" to HTML."""
    # ADD ELEMENTS (SVG favicon encoded with: https://yoksel.github.io/url-encoder/)
    pre_elements = r"""<!DOCTYPE html>
<html>
<head>
<title>Kindle Clippings</title>
<link href="data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8' standalone='no'%3F%3E%3C!-- Created with Inkscape (http://www.inkscape.org/) --%3E%3Csvg xmlns:dc='http://purl.org/dc/elements/1.1/' xmlns:cc='http://creativecommons.org/ns%23' xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns%23' xmlns:svg='http://www.w3.org/2000/svg' xmlns='http://www.w3.org/2000/svg' xmlns:sodipodi='http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd' xmlns:inkscape='http://www.inkscape.org/namespaces/inkscape' width='1000' height='1000' viewBox='0 0 264.58335 264.58335' version='1.1' id='svg8' inkscape:version='0.92.4 (5da689c313, 2019-01-14)' sodipodi:docname='klipps3.svg' inkscape:export-filename='C:%5CUsers%5Crafal%5CDesktop%5Cklipps.png' inkscape:export-xdpi='72.000008' inkscape:export-ydpi='72.000008'%3E%3Ctitle id='title3713'%3EKlipps%3C/title%3E%3Cdefs id='defs2' /%3E%3Csodipodi:namedview id='base' pagecolor='%23515151' bordercolor='%23000000' borderopacity='1' inkscape:pageopacity='0.20784314' inkscape:pageshadow='2' inkscape:zoom='0.35355339' inkscape:cx='-270.70393' inkscape:cy='554.94607' inkscape:document-units='px' inkscape:current-layer='layer3' showgrid='false' inkscape:window-width='3742' inkscape:window-height='2131' inkscape:window-x='2489' inkscape:window-y='-9' inkscape:window-maximized='1' units='px' inkscape:showpageshadow='false' showborder='true' inkscape:pagecheckerboard='false' showguides='true' inkscape:guide-bbox='true'%3E%3Csodipodi:guide position='132.29167,132.29167' orientation='0,1' id='guide3724' inkscape:locked='false' inkscape:label='' inkscape:color='rgb(0,0,255)' /%3E%3Csodipodi:guide position='132.29167,132.29167' orientation='1,0' id='guide3726' inkscape:locked='false' inkscape:label='' inkscape:color='rgb(0,0,255)' /%3E%3Csodipodi:guide position='79.375005,79.375005' orientation='-0.70710678,0.70710678' id='guide3748' inkscape:locked='false' inkscape:label='' inkscape:color='rgb(0,0,255)' /%3E%3Csodipodi:guide position='132.29167,132.29167' orientation='0.70710678,0.70710678' id='guide3750' inkscape:locked='false' inkscape:label='' inkscape:color='rgb(0,0,255)' /%3E%3Csodipodi:guide position='26.458327,150.45027' orientation='-0.70710678,0.70710678' id='guide3776' inkscape:locked='false' /%3E%3Csodipodi:guide position='150.45027,26.458323' orientation='-0.70710678,0.70710678' id='guide3778' inkscape:locked='false' /%3E%3Csodipodi:guide position='114.13307,238.12501' orientation='0.70710678,0.70710678' id='guide3780' inkscape:locked='false' inkscape:label='' inkscape:color='rgb(0,0,255)' /%3E%3Csodipodi:guide position='26.458335,150.45028' orientation='0.70710678,0.70710678' id='guide3782' inkscape:locked='false' inkscape:label='' inkscape:color='rgb(0,0,255)' /%3E%3Csodipodi:guide position='150.45028,26.458334' orientation='1,0' id='guide3801' inkscape:locked='false' /%3E%3Csodipodi:guide position='238.12501,114.13307' orientation='0,1' id='guide3803' inkscape:locked='false' /%3E%3Csodipodi:guide position='132.29167,114.13307' orientation='-0.70710678,0.70710678' id='guide3806' inkscape:locked='false' /%3E%3Csodipodi:guide position='26.458336,150.45028' orientation='0,1' id='guide3826' inkscape:locked='false' /%3E%3C/sodipodi:namedview%3E%3Cmetadata id='metadata5'%3E%3Crdf:RDF%3E%3Ccc:Work rdf:about=''%3E%3Cdc:format%3Eimage/svg+xml%3C/dc:format%3E%3Cdc:type rdf:resource='http://purl.org/dc/dcmitype/StillImage' /%3E%3Cdc:title%3EKlipps%3C/dc:title%3E%3Cdc:creator%3E%3Ccc:Agent%3E%3Cdc:title%3ERafał Karoń%3C/dc:title%3E%3C/cc:Agent%3E%3C/dc:creator%3E%3C/cc:Work%3E%3C/rdf:RDF%3E%3C/metadata%3E%3Cg inkscape:groupmode='layer' id='layer3' inkscape:label='Background' /%3E%3Cg inkscape:groupmode='layer' id='layer2' inkscape:label='Filling'%3E%3Ccircle style='fill:%23ffffff;stroke-width:0.22826612' id='path3736-9' cx='132.29167' cy='132.29169' r='114.13306' /%3E%3C/g%3E%3Cg inkscape:label='Icon' inkscape:groupmode='layer' id='layer1' transform='translate(0,-32.416632)'%3E%3Cpath style='fill:%2300ccff;stroke-width:1.32083833;fill-opacity:1' d='M 431.36914 100 L 100 431.36914 L 568.63086 900 L 568.63086 568.63086 L 900 568.63086 L 431.36914 100 z ' transform='matrix(0.26458335,0,0,0.26458335,0,32.416632)' id='rect3770' /%3E%3Cpath style='fill:%23000000;fill-opacity:1;stroke-width:1.32083833' d='M 500 500 L 500 831.36914 L 568.63086 900 L 568.63086 568.63086 L 900 568.63086 L 831.36914 500 L 500 500 z ' transform='matrix(0.26458335,0,0,0.26458335,0,32.416632)' id='rect3770-4' /%3E%3C/g%3E%3C/svg%3E%0A" rel='icon' type='image/svg'/>
</head>
<body>"""
    heading = "<h1>Kindle Clippings</h1>\n<h2>"
    footer = f"<footer>Generated on {datetime.datetime.now().strftime('%B %d, %Y')} at {datetime.datetime.now().strftime('%I:%M %p')} with <a target=\"_blank\" href=\"https://github.com/rafalkaron/Klipps\">Klipps</a></footer>"
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
    html_str = re.sub(r"<div class=\"entry\">\n<h2>\n<footer>", "</blockquote>\n</div>\n<footer>", html_str)    # Removes redundant entry divs and headers 2 before the footer
    html_str = re.sub("<div class=\"entry\">\n<h2>", "</blockquote>\n</div>\n<div class=\"entry\">\n<h2>", html_str)    # Closes blockquote and entry div before opening anothe entry div
    html_str = re.sub(r"</h1>\n<h2>", "</h1>\n<div class=\"entry\">\n<h2>", html_str)   # Opens the first element div after
    return html_str

def default_style_html_str(html_str):
    """Return a string that contains the \"Kindle Clippings.txt file\" converted to HTML with a default embedded CSS style."""
    html_str = re.sub("</h1>", "</h1>\n<div class=\"generator\"><p>Generated By Klipps</p></div>", html_str)
    html_str = re.sub("/>\n</head>", """/>
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
    
    footer{
        display: block;
        clear: both;
    }
    
    a{
        font-weight: bold;
        text-decoration: none;
    }

</style>
</head>""", html_str)
    return html_str

def custom_style_html_str(css_filepath, html_str):
    """Return a string that contains the \"Kindle Clippings.txt file\" converted to HTML with a custom embedded CSS style."""
    style = read_file(css_filepath)
    html_str = re.sub("/>\n</head>", f"/>\n<style>\n{style}\n</style>\n</head>", html_str)
    return html_str