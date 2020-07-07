import urllib
from urllib import request,parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class htmlDownloader(object):
#网页下载器
    def download(self,url):

        if url == None:
            return None

        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(url, context=context)
        # print("code:  ",response.getcode())
        if response.getcode() != 200:
            return None
        return response.read()

