"""feedshepherd text

Textual functions that are helpful when working with feeds
"""

import re
import unicodedata

from bs4 import BeautifulSoup


def slugify(value):
    """Given an arbitrary string, turn it into an acceptable slug

    >>> slugify('')
    ''
    >>> slugify('Hey folk$ what up? \t\t')
    'hey-folk-what-up'
    >>> slugify('CRAZY \u1234 String')
    'crazy-string'
    """
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("utf8")
    value = str(re.sub(r"[^\w\s-]", "", value).strip().lower())
    value = str(re.sub(r"[-\s]+", "-", value))
    return value


def parse_opml(fname):
    """For the given OPML file name, yield all feeds found as pairs of (name,
    url)."""
    with open(fname, encoding="utf-8") as opml:
        soup = BeautifulSoup(opml.read(), "lxml")
    for entry in soup.find_all("outline"):
        yield slugify(entry["text"]), entry["xmlurl"]
