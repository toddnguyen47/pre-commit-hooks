"""Utility functions"""

import re

from pre_commit_hooks import constants

_BEGINNING_HAS_TABS_PATTERN = re.compile(r"(^[ ]*)(\t+)([\S\s]*)$")
_BEGINNING_HAS_SPACES_PATTERN = re.compile(r"(^[\t]*)( +)([\S\s]*)$")


def contains_beginning_tabs(filename: str):
    """Check if `filename` contains tabs"""
    with open(filename, mode="rb") as file_checked:
        lines = file_checked.readlines()

    for line in lines:
        line = line.decode(encoding=constants.ENCODING)
        matcher = _BEGINNING_HAS_TABS_PATTERN.match(line)

        if matcher is not None:
            # If we match, that means there exists at least one tab
            return True

    return False


def contains_beginning_spaces(filename: str):
    """Check if `filename` contains spaces"""
    with open(filename, mode="rb") as file_checked:
        lines = file_checked.readlines()

    for line in lines:
        line = line.decode(encoding=constants.ENCODING)
        matcher = _BEGINNING_HAS_SPACES_PATTERN.match(line)

        if matcher is not None:
            # If we match, that means there exists at least one tab
            return True

    return False
