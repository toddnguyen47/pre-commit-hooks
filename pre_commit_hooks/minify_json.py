"""Minify JSON files / Make JSON files compact"""

import json
import argparse
from typing import Optional, Sequence
import sys

from pre_commit_hooks import json_helper, constants


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Main function to run"""
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to fix")
    args = parser.parse_args(argv)

    return_code = 0
    for filename in args.filenames:
        return_code = _handle_per_file(filename, return_code)

    return return_code


def _handle_per_file(filename: str, return_code: int) -> int:
    """Handle per file"""
    with open(filename, "r", encoding=constants.ENCODING) as curfile:
        data = curfile.read().strip()
        data_json = json.loads(data)
    # Ref: https://stackoverflow.com/a/33233406/6323360
    minified_json = json.dumps(
        data_json, separators=(",", ":"), ensure_ascii=False
    ).strip()
    output_return_code = json_helper.output_file(
        filename, data, minified_json, return_code
    )
    return_code = max(return_code, output_return_code)
    return return_code


if __name__ == "__main__":
    sys.exit(main())
