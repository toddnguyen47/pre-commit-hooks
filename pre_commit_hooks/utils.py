def contains_tabs(filename):
    with open(filename, mode="rb") as file_checked:
        return b"\t" in file_checked.read()
