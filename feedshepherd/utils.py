# TODO: utils modules are anti-patterns - when we're ready refactor everything out of here

import re
import unicodedata

from bs4 import BeautifulSoup
import requests


def slugify(value):
    value = unicodedata.normalize('NFKD', value).encode(
        'ascii', 'ignore').decode('utf8')
    value = str(re.sub('[^\w\s-]', '', value).strip().lower())
    value = str(re.sub('[-\s]+', '-', value))
    return value


# IMPORTANT: current directory should be our samples dir
def _find_sample_files():
    soup = BeautifulSoup(open('./DoggCatcherExport.opml').read(), 'lxml')
    for c in soup.find_all('outline'):
        print(c['text'])
        print(c['xmlurl'])
        feed_data = requests.get(c['xmlurl']).text
        fn = slugify(c['text']) + '.rss'
        print(f'Got {len(feed_data):,d} bytes for {fn}')
        with open(fn, 'w') as fh:
            fh.write(feed_data)
        print()
