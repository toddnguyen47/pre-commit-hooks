"""Convert text to HTML where each line is a <p> element"""

from typing import Optional, Sequence
import sys
import argparse
import os.path

import dominate
from dominate import tags

_DELIM = ","


def _generate_html_from_txt(
    doc_title: str, input_str: str, margin: float
) -> dominate.document:
    """Generate a simple HTML file from txt file"""
    doc = dominate.document(title=doc_title)

    with doc.head:
        css_style = _get_css_style(margin)
        tags.style(css_style)

    with doc:
        with tags.div(_class="content"):
            if input_str.strip():
                for line in input_str.split("\n"):
                    tags.p(line, _class="pmd-text")
            else:
                tags.p("You're good! No errors ✨ 🍰 ✨", _class="pmd-text")

    return doc


def _get_css_style(margin: float) -> str:
    """Generate CSS style"""
    with_margin_str = f"margin-left:{margin}em;margin-right:{margin}em"
    style_list = [
        r"*,*::after,*::before{box-sizing:border-box}body{font-size:1rem}",
        r"p.pmd-text{font-family:monospace}div.content{margin-left:0;margin-right:0}",
        r"@media (min-width: 600px)",
        r"{div.content",
        r"{" + with_margin_str + r"}",
        r"}",
    ]
    return "".join(style_list)


def _handle_file(file_path: str, margin: float):
    """Convert current file to HTML"""
    data = ""
    with open(file_path, "r") as input_file:
        data = input_file.read()
    head, tail = os.path.split(file_path)
    root, _extension = os.path.splitext(tail)
    html_str = _generate_html_from_txt(root, data, margin)
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
    parser.add_argument(
        "--margin",
        help="optional float `em` value to use as margin. Defaults to `10em`",
        default=10,
    )
    args = parser.parse_args(argv)

    comma_sep_files = args.textfiles
    list_of_files = comma_sep_files.split(_DELIM)
    for index, file1 in enumerate(list_of_files):
        list_of_files[index] = file1.strip()

    for file_path in list_of_files:
        _handle_file(file_path, args.margin)

    return 0


if __name__ == "__main__":
    sys.exit(main())
