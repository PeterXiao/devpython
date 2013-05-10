
import urllib2
def parse(url,size=10):
    """Return entries of feed."""
    result = urllib2.Request(url)
    print result

url = 'www.baidu.com'
parse(url)