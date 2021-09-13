"""Common Constants"""

import re

ENCODING = "utf-8"

# Import this pattern on https://regex101.com/ for detailed explanation
_BEGINNING_TABS_STR = r"(^[ \t]+)([\S\s]*)"
BEGINNING_TABS_PATTERN = re.compile(_BEGINNING_TABS_STR)
