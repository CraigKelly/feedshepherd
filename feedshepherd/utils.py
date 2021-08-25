"""feedshepherd utils

TODO: utils modules are anti-patterns - when we're ready refactor everything
out of here
"""

import re
import unicodedata

from bs4 import BeautifulSoup
import requests


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


# IMPORTANT: current directory should be our samples dir
def _find_sample_files():
    with open("./DoggCatcherExport.opml", encoding="utf-8") as opml:
        soup = BeautifulSoup(opml.read(), "lxml")
    for entry in soup.find_all("outline"):
        print(entry["text"])
        print(entry["xmlurl"])
        feed_data = requests.get(entry["xmlurl"]).text
        fname = slugify(entry["text"]) + ".rss"
        print(f"Got {len(feed_data):,d} bytes for {fname}")
        with open(fname, "w", encoding="utf-8") as feed_file:
            feed_file.write(feed_data)
        print()
