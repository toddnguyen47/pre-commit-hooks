"""Utility functions"""

from typing import List

from pre_commit_hooks import constants


def contains_beginning_tabs(filename: str):
    """Check if `filename` contains tabs"""
    with open(filename, mode="rb") as file_checked:
        lines = file_checked.readlines()
    return _contains_beginning_char_helper(lines, "\t")


def contains_beginning_spaces(filename: str, comment_char: str):
    """Check if `filename` contains spaces"""
    with open(filename, mode="rb") as file_checked:
        lines = file_checked.readlines()
    return _contains_beginning_char_helper(lines, " ", comment_char)


def _contains_beginning_char_helper(
    lines: List[str], char_to_find: str, comment_char: str = ""
) -> bool:
    found_char = False
    for (line_num, line) in enumerate(lines):
        line = line.decode(encoding=constants.ENCODING)
        if line.strip() == "":
            continue

        beginning_whitespace_list_with_comment_char = []
        for char1 in line:
            if char1.isspace():
                beginning_whitespace_list_with_comment_char.append(char1)
            else:
                # Found a non-whitespace character. Append the character to our list, as it is a possible
                # comment starter, then break out of the loop
                beginning_whitespace_list_with_comment_char.append(char1)
                break

        for (index, char1) in enumerate(beginning_whitespace_list_with_comment_char):
            if char1 == char_to_find:
                next_char = beginning_whitespace_list_with_comment_char[index + 1]
                found_char = not (char1 == " " and next_char == comment_char)

        if found_char:
            print(f"OFFENDING LINE: Line number {line_num + 1}")
            print(line)
            break
    return found_char
