# import urllib
# from urllib import request,parse
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
#
# class htmlDownloader(object):
# #网页下载器
#     def download(self,url):
#
#         if url == None:
#             return None
#
#         context = ssl._create_unverified_context()
#         response = urllib.request.urlopen(url, context=context)
#         # print("code:  ",response.getcode())
#         if response.getcode() != 200:
#             return None
#         return response.read()
#


#用requests请求数据
import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class htmlDownloader(object):
#网页下载器
    def download(self,url):

        if url == None:
            return None
        #注意要写headers 不然请求下来的数据不全
        headers = {
            'user-agent': 'Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 53.0.2785.104Safari / 537.36Core / 1.53.4882.400QQBrowser / 9.7.13059.400'
        }
        response = requests.get(url,headers = headers)
        print(response.status_code)

        print(response.text)

        if response.status_code != 200:
            return None
        return response.text
