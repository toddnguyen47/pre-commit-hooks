"""Utility functions"""

import re

# Import this pattern on https://regex101.com/ for detailed explanation
BEGINING_TABS_PATTERN: re.Pattern = re.compile(r"(^[ \t]+)([\S\s]*)")


def contains_beginning_tabs(filename: str):
    """Check if `filename` contains tabs"""
    with open(filename, mode="rb") as file_checked:
        lines = file_checked.readlines()

    for line in lines:
        matcher = BEGINING_TABS_PATTERN.match(line)

        if matcher is None:
            return True

    return False
