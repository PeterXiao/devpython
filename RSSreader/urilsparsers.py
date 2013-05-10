__author__ = 'Administrator'
import urllib2
import urlparse
from  feedparser import parse as feedparse
from itertools import islice
from itertools import imap
def _filter_entry(entry):
    '''Filters entry filends'''
    entry['links']=[link['href'] for link in entry['links']]
    return entry
def parse(url,size=10):
    """Return entries of feed."""
    result = feedparse(url)
    return islice(imap(_filter_entry(),result['entries'],size))
