def save_file(file):
    """Saves a new file"""
    open(str(_out_folder) + "/" + "out_" +str(_timestamp.strftime("%d_%m_%y-%H-%M-%S")) + ".html", "w")

def append_to_file(file):
    """Appends a string to a file"""

