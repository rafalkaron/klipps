__author__ = 'Rafał Karoń <rafalkaron@gmail.com>'

def progressbar(prefix, fill, length, percent):
    """Prints a progress bar"""
    percent_fraction = percent/100
    fill = "".join([fill for _ in range(int(length*percent_fraction))])
    body = f"{prefix} [{fill}] {percent}%"
    if percent < 100:
        print(body, end="\r", flush="true")
    if percent == 100:
        print(body)
    