"""Convert beginning spaces"""

# region imports
# *********************************************************
import argparse
import sys
from typing import List

from pre_commit_hooks import constants, convert_beginning_helper, utils

# endregion


def convert_file(full_path: str, num_spaces: int):
    """Convert a file's beginning spaces to tabs"""
    convert_beginning_helper.read_file_convert(full_path, num_spaces, handle_per_line)


def handle_per_line(lines: List[str], num_spaces: int):
    """Handle per line and return an encoded string"""
    line = lines.popleft()
    line = line.decode(encoding=constants.ENCODING)
    converted_line = convert_spaces_to_tabs(line, num_spaces)
    encoded_line = (converted_line + "\n").encode(constants.ENCODING)
    return encoded_line


def convert_spaces_to_tabs(input_line: str, num_spaces: int) -> str:
    """Convert spaces to tabs"""

    # GUARD: If input_line is just an empty line, then return early.
    if input_line.strip() == "":
        return ""

    only_whitespace_list = []
    remaining_str = ""
    for (index, char1) in enumerate(input_line):
        if char1.isspace():
            only_whitespace_list.append(char1)
        else:
            remaining_str = input_line[index:]
            break

    space_str = _generate_space_str(num_spaces)
    only_whitespace_str = "".join(only_whitespace_list)
    only_whitespace_str = only_whitespace_str.replace(space_str, "\t")
    # now, remove any leftover whitespace
    only_whitespace_str = only_whitespace_str.replace(" ", "")

    return_str = only_whitespace_str + remaining_str
    return_str = return_str.rstrip()
    return return_str


def _generate_space_str(num_spaces: int) -> str:
    """Generate spaces str"""
    spaces_list = []
    for _ in range(num_spaces):
        spaces_list.append(" ")
    return "".join(spaces_list)


def main(argv=None):
    """Ref: https://github.com/Lucas-C/pre-commit-hooks/blob/master/pre_commit_hooks/remove_tabs.py"""
    parser = argparse.ArgumentParser()
    parser = convert_beginning_helper.add_tab_size_option(parser)
    parser.add_argument(
        "--comment-char",
        required=False,
        help="the comment character to detect. Will ignore exactly ONE space preceding this comment character",
    )
    parser.add_argument("filenames", nargs="*", help="filenames to check")
    args = parser.parse_args(argv)

    files_with_tabs = [
        file1
        for file1 in args.filenames
        if utils.contains_beginning_spaces(file1, args.comment_char)
    ]

    for file_with_tabs in files_with_tabs:
        print(f"In {file_with_tabs}, substituting {args.tab_size} spaces with tabs")
        convert_file(file_with_tabs, args.tab_size)

    if files_with_tabs:
        print("")
        print(
            "Beginning spaces have been successfully removed. Now aborting the commit."
        )
        return convert_beginning_helper.print_check_changes_message()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
