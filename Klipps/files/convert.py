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
    heading = "# Kindle Clippings"
    md_str = re.sub("==========", "\n---\n", md_str)
    md_str = re.sub(r"- Your Highlight at location.* \| ", "", md_str)

    for added_on in re.findall(r"^Added on .*,*. \d.* \d\d:\d\d:\d\d$", md_str, re.MULTILINE):
        added_on_new = f"*{added_on}*"
        md_str = re.sub(added_on, added_on_new, md_str)
    
    footer = f"Generated on {timestamp.strftime('%B %d, %Y')} at {timestamp.strftime('%-I:%-M %p')} with [Klipps](https://github.com/rafalkaron/Klipps/releases)."
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
    head = "<head>\n<title>Kindle Clippings</title>\n<link href='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAEBXpUWHRSYXcgcHJvZmlsZSB0eXBlIGV4aWYAAHjarVdtlqwoDP2fVcwSTEL4WA4KnDM7mOXPBakv266y+z05mpiCS8gNwaL637+N/sElSxJyFqJP3i+4XHJJMpS47NcueXHjOV+Wm/Jip/sPApNC6v7q6+yfYbfHgOCmfX21U9gmTpxAN+QJqH1mgVKmkxNIZbfzfKcku5L903Lm3TZJ3WTr/tPx3QUEoxjwVEiqsi77c59J9zvjdniKOnRk1WGR8Uxf40fLcwwPAbxrh/gt27TrIxw70G1Z/hCnaWc7j9+I0rNHLPeZ5YVqXcLyfD3Hr5XYWt1Xl50nhMvPRd2WMjR0REidjmEeLeA26GG0hBaXvGxgrWCpKy0rXhILZm/suHDmxnXIjTe46KRKgBTZRIctapAkm3YKXG/cJJAmLRrBxgbmFGa5+8Jj3tTnw2QRMxdGT2GAMUa8NDoafttegFrrac68xHus4Jf0lIUbnbn+RC8Qwm3G1EZ8mXaxHK9OrIJBG2GOWGBe1h1iNX7klg6edTFCV7fs+4VDmQAIEeY2OMMKBhbPaux5CSKBGXGM4CfD8572KxhgI5MCL8WpepATpc+NMYFHXzHZzSgvIMLUawA1STPIcs6cx36LSKFMpubMzFuwaMmyV++8ee+D73UqBw0uWPAhhBhSyFGjixZ9DDHGFHOSpChjRsmnkGJKKWdMml0GVkb/DMMqq65utdWvYY1rWvOG9NncZpvfwha3tOUiRQtKABVfQokllVy5IpWqq1Z9DTXWVHNDrjVtrlnzLbTYUst31iarr6wdmXvPGk/WZBDV+4UHazCHcIPgXk6scwbGxDEYD50BJLR0zpbIzklnrnOG2q+kagIvrZNTuDMGBl1lscZ37h7MfcsbIbo/5U3OmKNO3d9gjjp1T8x95e2EtZJHudVBUN+FiCkqpGL7oUONWWLu59K5bGvxQ3WGzeOsn0NPko6GM4mcsV3dkAYDeTlKOhq0Nhtqwm7tY60fgp8lXe3YZdjYhqoowIeV09nSy827KLsm8RHEZqdhpNO45pvaZKtt6onbGw/pDSnYsFPlun4ihD51eKBaKxMVaf2FTkrvaELmTjXk7W4sYa4xJLmPoI9EXYSiC5xfgqJL6XMBii5m4kcoupzUH6BI+O9A0TOFfwJFr9nweyg6JtZvoehrjv4Ois7S/TdQdL5zfg5F32zCsNUyVHzqxxx2q2pNc4OnO9REpUtb+4KD9D7zT8PxBaePoLdD3vr3XGjbSr8rsL1e2ku9pDm0XBn6vtS+OxnP17vGHTE2/O1wdR8EoG9jmGS6kLmq3QDd+3r07hD98PmwS7p2GH3+vKDvvy9+9nlBf/75sEsa/xXxr5n+B+M9pshtgWrgAAABhGlDQ1BJQ0MgUFJPRklMRQAAeJx9kT1Iw0AcxV/TSqVUHOyg4pChOlkQFXXUKhShQqkVWnUwufQLmjQkKS6OgmvBwY/FqoOLs64OroIg+AHi5Oik6CIl/i8ptIjx4Lgf7+497t4BQqPCVDMwBqiaZaQTcTGbWxWDrwigHyFMY0Bipj6XSiXhOb7u4ePrXYxneZ/7c/QoeZMBPpF4lumGRbxBPLVp6Zz3iSOsJCnE58SjBl2Q+JHrsstvnIsOCzwzYmTS88QRYrHYwXIHs5KhEk8SRxVVo3wh67LCeYuzWqmx1j35C8N5bWWZ6zSHkMAilpCCCBk1lFGBhRitGikm0rQf9/APOv4UuWRylcHIsYAqVEiOH/wPfndrFibG3aRwHOh6se2PYSC4CzTrtv19bNvNE8D/DFxpbX+1Acx8kl5va9EjoHcbuLhua/IecLkD9D/pkiE5kp+mUCgA72f0TTmg7xYIrbm9tfZx+gBkqKvkDXBwCIwUKXvd493dnb39e6bV3w+RA3Kz5tCL4AAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAAuIwAALiMBeKU/dgAAAAd0SU1FB+QEGAsCCWaTH0MAAAELSURBVDjLrZOxSsRAFEXPTGwCyQ/Y7gdY2oimthbWehFBiLCiCBaiVqkEwXQbrBPwHzLBRgRhU1mlXT9gF7YLNi8S1jFI1lPOvPuGue8+xQrLxXwPGAIBMJDjCjBA5np+0a5XLeEmcAWEdBMDkev5s+8GIr6v6/rwtXjhaXxjVY4e7tje3cFxnBQ4dz1/1jR4BMKjrYC/kJQGIHY9/3RD/hxaCn6w8kC4XMyftRjWl6EWt/sS6Nao+jDQrImWkPSl0pIwK9H4kuvRSVcDo4Hst5FV+Ruf7x905CPTku3YNu/JNGcyzW0ZaIJUNCZGQNrcHNyekZQGpRRKKZLSsH9x3BanovmnZVpnnb8AdTJc9zo6ejgAAAAASUVORK5CYII='rel='icon' type='image/png'/></head>"
    body_open = "<body>"
    body_close = "</body>"
    html_str = "\n".join((html_declaration, html_tag_open, head, body_open, html_str, body_close, html_tag_close))

    html_str = re.sub("<body>", "<body style=\"width:60%; background-color: #F7F4F3; margin:auto; font-family: \'Helvetica Neue\', Helvetica, Arial, sans-serif;\">", html_str)
    html_str = re.sub("<h1>", "<h1 style=\"margin-top:10px;margin-bottom:5px;font-weight:normal; font-size:400%; color:#5B2333; border-bottom: 5px solid #564D4A;\">", html_str)
    html_str = re.sub("<hr>", "<hr style=\"background-color:#564D4A\">", html_str)
    html_str = re.sub("<h2>", "<h2 style=\"color:BA1B1D\">", html_str)
    html_str = re.sub("<a href=", "<a target='blank' style='text-decoration: none; color:#5B2333; font-weight:bold'href=", html_str)
    return html_str

def save_str_as_file(str, filepath):
    """Save a string as a file"""
    out = filepath
    with open(out, "w") as file:
        file.write(str)
    return out