"""Convert beginning spaces"""

# region imports
# *********************************************************
import sys
import argparse
from collections import deque

from pre_commit_hooks import utils, constants

# endregion

_TABS_CHAR = "\t"


def convert_file(full_path: str, num_spaces: int):
    """Convert a file's beginning spaces to tabs"""
    # We need to open using binary and encode/decode appropriate to enforce that files need to be saved
    # with Linux line endings
    with open(full_path, mode="rb") as input_file:
        lines = input_file.readlines()
    lines = deque(lines)
    new_lines = []
    while lines:
        line = lines.popleft()
        line = line.decode(encoding=constants.ENCODING)
        converted_line = convert_spaces_to_tabs(line, num_spaces)
        new_lines.append((converted_line + "\n").encode(constants.ENCODING))

    with open(full_path, mode="wb") as output_file:
        output_file.writelines(new_lines)


def convert_spaces_to_tabs(input_line: str, num_spaces: int) -> str:
    """Convert spaces to tabs"""
    only_whitespace_list = []
    remaining_str = ""
    for (index, char1) in enumerate(input_line):
        if char1.isspace():
            only_whitespace_list.append(char1)
        else:
            remaining_str = input_line[index:]
            break
    remaining_str = remaining_str.rstrip()

    space_str = _generate_space_str(num_spaces)
    only_whitespace_str = "".join(only_whitespace_list)
    only_whitespace_str = only_whitespace_str.replace(space_str, "\t")

    return_str = only_whitespace_str + remaining_str
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
    parser.add_argument(
        "--tab-size",
        type=int,
        required=False,
        help="number of whitespaces to be replaced by tabs. defaults to 4 spaces",
        default=4,
        dest="tab_size",
    )
    parser.add_argument("filenames", nargs="*", help="filenames to check")
    args = parser.parse_args(argv)

    files_with_tabs = [
        file1 for file1 in args.filenames if utils.contains_beginning_spaces(file1)
    ]

    for file_with_tabs in files_with_tabs:
        print(f"In {file_with_tabs}, substituting {args.tab_size} spaces with tabs")
        convert_file(file_with_tabs, args.tab_size)

    if files_with_tabs:
        print("")
        print(
            "Beginning spaces have been successfully removed. Now aborting the commit."
        )
        print(
            'You can check the changes made. Then simply "git add --update ." and re-commit'
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
