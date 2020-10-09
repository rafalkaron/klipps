def read_file_lines(file):
    """Returns a list of str lines in text file"""
    with open(file, mode="rt", encoding="utf-8") as f:
        return f.readlines()
