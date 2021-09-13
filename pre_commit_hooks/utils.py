"""Utility functions"""

from pre_commit_hooks import constants

def contains_beginning_tabs(filename: str):
    """Check if `filename` contains tabs"""
    with open(filename, mode="rb") as file_checked:
        lines = file_checked.readlines()

    for line in lines:
        line = line.decode(encoding=constants.ENCODING)
        matcher = constants.BEGINNING_TABS_PATTERN.match(line)

        if matcher is not None:
            return True

    return False
