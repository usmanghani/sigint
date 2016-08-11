START = 0 # start at this index
LIMIT = 5 # download this many items


import feedparser
import pprint
from itertools import chain


# feed = feedparser.parse('feed://feeds.soundcloud.com/users/soundcloud:users:38128127/sounds.rss')
feed = feedparser.parse('startalk.xml')

with open('bingo.txt', 'w') as f:
    f.write(pprint.pformat(feed))

# print (feed['entries'][0]['links'])

audio_urls = list(chain(*[map(lambda x: x['href'], filter(lambda x: 'audio' in x.get('type'), entry['links'])) for entry in feed['entries']]))

import eventlet
requests = eventlet.import_patched('requests')

pool = eventlet.GreenPool()
import os
import urlparse


def get_asset(asset_url):
    print asset_url
    return os.path.basename(urlparse.urlparse(asset_url).path), requests.get(asset_url, stream=True)

for file_name, audio_file_content in pool.imap(get_asset, audio_urls[START: START + LIMIT]):
    with open(file_name, 'wb') as f:
        f.write(audio_file_content.content)

    print "Done writing %s" % file_name

