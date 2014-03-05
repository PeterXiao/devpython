__author__ = 'Administrator'
import gevent
from gevent import monkey, Greenlet
monkey.patch_all()
from pyquery import PyQuery as pq
from urllib import urlretrieve


MAX_PAGE = 45
Template = "http://www.fengyun5.com/Sibao/600/%d.html"


def download_meizi(page_url):
    try:
         d = pq(url=page_url)
         img_url = d('#content img').attr("src")
         img_name = img_url.split("/")[-1]
         print("Downloading:", img_url)
         urlretrieve(img_url, img_name)
    except:
        print("Download: %s error!" % page_url )
    pass


threads = [Greenlet.spawn(download_meizi, Template % i) for i in range(MAX_PAGE)]
gevent.joinall(threads)
print("Done!")