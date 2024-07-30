"""Prettify JSON files"""

import json
import argparse
from typing import Optional, Sequence
import sys

from pre_commit_hooks import constants, json_helper


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Main function to run"""
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to fix")
    parser.add_argument(
        "--indent", type=int, help="Number of spaces to indent", default=2
    )
    args = parser.parse_args(argv)
    spaces_indent = int(args.indent)

    return_code = 0
    for filename in args.filenames:
        return_code = _handle_per_file(filename, spaces_indent, return_code)

    return return_code


def _handle_per_file(filename: str, spaces_indent: int, return_code: int) -> int:
    """Handle per file"""
    with open(filename, "r", encoding=constants.ENCODING) as curfile:
        data = curfile.read().strip()
        data_json = json.loads(data)
    prettified_json = json.dumps(
        data_json, indent=spaces_indent, ensure_ascii=False
    ).strip()
    output_return_code = json_helper.output_file(
        filename, data, prettified_json, return_code
    )
    return_code = max(return_code, output_return_code)
    return return_code


if __name__ == "__main__":
    sys.exit(main())
