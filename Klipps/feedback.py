__author__ = 'Rafał Karoń <rafalkaron@gmail.com>'

def progressbar(prefix: str, fill: str, length: int, percent: int):
    fill = "".join([fill for _ in range(int(length/percent))])
    print(f"{prefix} [{fill}] {percent}%", end="\r", flush="true")