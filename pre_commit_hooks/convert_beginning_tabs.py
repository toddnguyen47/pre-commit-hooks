"""Convert Beginning Tabs to Spaces Module"""

# region imports
# *********************************************************
import os
import argparse
import sys
from collections import deque

from pre_commit_hooks import utils, constants

# endregion imports

_TMP_FILE = "tmp"
_SPACE_CHAR = " "
_INDEX_GROUP_ONLY_SPACES_AND_TABS = 1
_INDEX_GROUP_REMAINING_CHARACTERS = 2


def convert_on_files_with_ext(
    file_path: str, num_spaces: int, file_extension: str = ""
):
    """Convert beginning tabs to spaces in files in `file_path`.

    Args:
        `file_path (str)`: The path where your files are located. Note that this function will recursively walk
        starting from this file_path.

        `num_spaces (int)`: Number of spaces used to replace beginning tabs with.

        `file_extension (str)`: Optional. If not given, all files will have their beginning tabs converted to
        spaces. If given, only the files with those extensions will have their beginning tabs converted. You do
        not need to include the period (.) in the extension. Simply pass in `java` instead of `.java`. Also,
        this extension is NOT case sensitive.
    """
    file_extension = file_extension.strip().lower()
    for root, _, files in os.walk(file_path):
        for file in files:
            file_name_lowercase = file.lower()
            if file_name_lowercase.endswith(file_extension):
                full_path = os.path.join(root, file)
                convert_file_with_temp_output_file(full_path, num_spaces)

def convert_file_with_temp_output_file(full_path: str, num_spaces: int):
    """Convert file with beginning tabs to spaces. This function will write to a temporary file instead of
    storing it in buffer."""
    print("Operating on '{}'".format(full_path.replace("\\", "/")))
    # We need to open using binary and encode/decode appropriate to enforce that files need to be saved
    # with Linux line endings
    with open(full_path, mode="rb") as input_file:
        with open(_TMP_FILE, mode="wb") as output_file:
            for line in input_file:
                line = line.decode(encoding=constants.ENCODING)
                converted_line = convert_tabs_to_spaces(line, num_spaces)
                output_file.write((converted_line + "\n").encode(constants.ENCODING))
    _overwrite_input_file(full_path)

def convert_file(full_path: str, num_spaces: int):
    """Convert a file's beginning tabs to spaces"""
    # We need to open using binary and encode/decode appropriate to enforce that files need to be saved
    # with Linux line endings
    with open(full_path, mode="rb") as input_file:
        lines = input_file.readlines()
    lines = deque(lines)
    new_lines = []
    while lines:
        line = lines.popleft()
        line = line.decode(encoding=constants.ENCODING)
        converted_line = convert_tabs_to_spaces(line, num_spaces)
        new_lines.append((converted_line + "\n").encode(constants.ENCODING))

    with open(full_path, mode="wb") as output_file:
        output_file.writelines(new_lines)

def convert_tabs_to_spaces(input_line: str, num_spaces: int) -> str:
    """Convert tabs to spaces of the current `input_line`"""
    matcher = constants.BEGINNING_TABS_PATTERN.match(input_line)
    return_str = ""

    if matcher is None:
        return_str = input_line
    else:
        tabs_str = matcher.group(_INDEX_GROUP_ONLY_SPACES_AND_TABS)
        space_str = _replace_tabs_with_respect_to_beginning_spaces(
            tabs_str, num_spaces
        )
        return_str = space_str + matcher.group(_INDEX_GROUP_REMAINING_CHARACTERS)

    return return_str.rstrip()


def _replace_tabs_with_respect_to_beginning_spaces(
    tabs_str: str, num_spaces: int
) -> str:
    """Will replace tabs with respect to space in front of it.
    Let's use `s` for spaces and `t` for tabs.
    For example, if the input string is `st`, and the tabsize is 4, then that tab should only be replaced
    by 3 tabs.
    """
    # space_per_tab = _generate_space(num_spaces)
    # space_str = tabs_str.replace("\t", num_spaces)
    num_preceding_spaces = 0
    output_str = ""
    for char in tabs_str:
        if char == " ":
            num_preceding_spaces += 1
            # Reset num_preceding_spaces if it ever exceeds the provided num_spaces
            if num_preceding_spaces >= num_spaces:
                num_preceding_spaces = 0
            output_str = output_str + char
        elif char == "\t":
            num_spaces_to_use = num_spaces - num_preceding_spaces
            space_str = _generate_space(num_spaces_to_use)
            output_str = output_str + space_str
            num_preceding_spaces = 0
        else:
            raise RuntimeError("Not a space or tab in `tabs_str`!")
    return output_str


def _overwrite_input_file(full_path: str):
    """Overwrite input file with temp file"""
    os.remove(full_path)
    os.rename(_TMP_FILE, full_path)


def _generate_space(num_spaces: int) -> str:
    """Generate the correct amount of spaces per tab"""
    list1 = []
    return_str_with_only_spaces = ""
    for _ in range(num_spaces):
        list1.append(_SPACE_CHAR)
    return return_str_with_only_spaces.join(list1)


def main(argv=None):
    """Ref: https://github.com/Lucas-C/pre-commit-hooks/blob/master/pre_commit_hooks/remove_tabs.py"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--whitespaces-count",
        type=int,
        required=False,
        help="number of whitespaces to substitute tabs with. defaults to 4 spaces",
        default=4,
    )
    parser.add_argument("filenames", nargs="*", help="filenames to check")
    args = parser.parse_args(argv)

    files_with_tabs = [file1 for file1 in args.filenames if utils.contains_beginning_tabs(file1)]

    for file_with_tabs in files_with_tabs:
        print(
            "Substituting tabs in: {0} by {1} whitespaces".format(
                file_with_tabs, args.whitespaces_count
            )
        )
        convert_file(file_with_tabs, args.whitespaces_count)

    if files_with_tabs:
        print("")
        print("Beginning tabs have been successfully removed. Now aborting the commit.")
        print(
            'You can check the changes made. Then simply "git add --update ." and re-commit'
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
