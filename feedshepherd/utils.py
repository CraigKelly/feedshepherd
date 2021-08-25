"""feedshepherd utils

TODO: utils modules are anti-patterns - when we're ready refactor everything
out of here
"""

import requests

from .text import parse_opml

# IMPORTANT: current directory should be our samples dir
def _find_sample_files():
    for name, url in parse_opml("./DoggCatcherExport.opml"):
        print(name)
        print(url)
        feed_data = requests.get(url).text
        fname = f"{name}.rss"
        print(f"Got {len(feed_data):,d} bytes for {fname}")
        with open(fname, "w", encoding="utf-8") as feed_file:
            feed_file.write(feed_data)
        print()
