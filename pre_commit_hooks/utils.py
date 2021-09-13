"""Utility functions"""

import re

# Import this pattern on https://regex101.com/ for detailed explanation
BEGINNING_TABS_STR = r"(^[ \t]+)([\S\s]*)"
_BEGINNING_TABS_PATTERN = re.compile(BEGINNING_TABS_STR)


def contains_beginning_tabs(filename: str):
    """Check if `filename` contains tabs"""
    with open(filename, mode="rb") as file_checked:
        lines = file_checked.readlines()

    for line in lines:
        matcher = _BEGINNING_TABS_PATTERN.match(line)

        if matcher is None:
            return True

    return False
