"""Helper functions for converting beginning whitesspace characters"""

import argparse
from collections import deque
from typing import Callable, List


def add_tab_size_option(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    """Add the `--tab-size` option"""
    parser.add_argument(
        "--tab-size",
        type=int,
        required=False,
        help="number of whitespaces to substitute tabs with. defaults to 4 spaces",
        default=4,
        dest="tab_size",
    )
    return parser


def read_file_convert(
    full_path: str,
    num_spaces: int,
    comment_char: str,
    handle_per_line: Callable[[List[str], int, str], str],
):
    """Read file and convert its beginning whitespace per line"""
    lines = _read_lines_rb(full_path)
    new_lines = []
    while lines:
        encoded_str = handle_per_line(lines, num_spaces, comment_char)
        new_lines.append(encoded_str)

    with open(full_path, mode="wb") as output_file:
        output_file.writelines(new_lines)


def _read_lines_rb(full_path: str) -> deque:
    """
    We need to open using binary and encode/decode appropriate to enforce that files need to be saved
    with Linux line endings
    """
    with open(full_path, mode="rb") as input_file:
        lines = input_file.readlines()
    lines = deque(lines)
    return lines


def print_check_changes_message():
    """Print check changes message"""
    print(
        'You can check the changes made. Then simply "git add --update ." and re-commit'
    )
    return 1
