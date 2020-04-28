__author__ = 'Rafał Karoń <rafalkaron@gmail.com>'

def progressbar(percent, length=50, prefix="Processing", fill="#", empty="-"):
    """Call the function to print a progress bar.
    

    """
    
    empty_number = length-length*(percent/100)
    fill = "".join([fill for _ in range(int(length*(percent/100)))])
    empty = "".join([empty for _ in range(int(empty_number))])
    body = f"{prefix} [{fill}{empty}] {percent}%"
    if percent < 100:
        print(body, end="\r", flush="true")
    if percent == 100:
        print(body)