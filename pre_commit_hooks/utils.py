"""Utility functions"""


def contains_tabs(filename: str):
    """Check if `filename` contains tabs"""
    with open(filename, mode="rb") as file_checked:
        return b"\t" in file_checked.read()
