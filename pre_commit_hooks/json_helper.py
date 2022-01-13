"""Helper file for functions used in `minify_json` and `prettify_json`"""

from typing import Any

from pre_commit_hooks import constants

_ERROR_CODE_JSON_FILES_WRITTEN = 1


def output_file(filename: str, data: Any, fixed_json: Any):
    """Output to file"""
    if data != fixed_json:
        return_code = max(return_code, _ERROR_CODE_JSON_FILES_WRITTEN)
        with open(filename, "w", encoding=constants.ENCODING) as curfile:
            curfile.write(fixed_json)
            curfile.write("\n")
    return return_code
