"""Convert text to HTML where each line is a <p> element"""

from typing import Optional, Sequence
import sys
import argparse
import os.path

import dominate
from dominate import tags

_DELIM = ","


def _generate_html_from_txt(doc_title: str, input_str: str) -> dominate.document:
    """Generate a simple HTML file from txt file"""
    doc = dominate.document(title=doc_title)

    with doc.head:
        tags.style(
            r"html{font-size:62.5%;}body{font-size:1.8rem;}div.content{width:1024px;margin:auto;}"
            + r"p.pmd-text{font-family:monospace;}"
        )

    with doc:
        with tags.div(_class="content"):
            if input_str.strip():
                for line in input_str.split("\n"):
                    tags.p(line, _class="pmd-text")
            else:
                tags.p("You're good! No errors ✨ 🍰 ✨", _class="pmd-text")

    return doc

def _handle_file(file_path: str):
    """Convert current file to HTML"""
    data = ""
    with open(file_path, "r") as input_file:
        data = input_file.read()
    head, tail = os.path.split(file_path)
    root, _extension = os.path.splitext(tail)
    html_str = _generate_html_from_txt(root, data)
    outfile = os.path.join(head, root + ".html")
    with open(outfile, "w") as output_file:
        output_file.write(str(html_str))


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Main Function"""
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to fix")
    parser.add_argument(
        "--textfiles", help="comma separated list of text files to convert"
    )
    args = parser.parse_args(argv)

    comma_sep_files = args.textfiles
    list_of_files = comma_sep_files.split(_DELIM)
    for index, file1 in enumerate(list_of_files):
        list_of_files[index] = file1.strip()

    for file_path in list_of_files:
        _handle_file(file_path)

    return 0


if __name__ == "__main__":
    sys.exit(main())
