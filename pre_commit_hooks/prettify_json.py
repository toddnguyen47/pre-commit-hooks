"""Prettify JSON files"""

import json
import argparse
from typing import Optional, Sequence
import sys

_ENCODING = "utf-8"
_ERROR_CODE_JSON_FILES_WRITTEN = 1


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Main function to run"""
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to fix")
    parser.add_argument("--indent", type=int, help="Number of spaces to indent")
    args = parser.parse_args(argv)

    return_code = 0
    for filename in args.filenames:
        with open(filename, "r", encoding=_ENCODING) as curfile:
            data = curfile.read().strip()
            data_json = json.loads(data)
        spaces_indent = int(args.indent)
        prettified_json = json.dumps(data_json, indent=spaces_indent).strip()
        if data != prettified_json:
            return_code = max(return_code, _ERROR_CODE_JSON_FILES_WRITTEN)
            with open(filename, "w", encoding=_ENCODING) as curfile:
                curfile.write(prettified_json)
                curfile.write("\n")

    return return_code


if __name__ == "__main__":
    sys.exit(main())
