

#import urllib2 报错
#python3不能使用urllib2解决办法
import urllib.request as urllib2
import ssl
import urllib
from http import cookiejar
import json
from urllib import parse

#1
context = ssl._create_unverified_context()
reponse = urllib2.urlopen('https://www.baidu.com', context=context)
print(reponse.getcode())
print(reponse.read())

#
# #2 下载网页方法2 添加data，http header
# # 设置data有点问题
# url = 'http://www.baidu.com'
# # 需要登陆的账户密码
# dict = {"email": "xxxxxx", "password": "xxxxx"}
# headers = {'token':'12343'}
# data = bytes(parse.urlencode(dict), encoding='utf8')
# # data = urllib.urlencode(dict)
# request = urllib2.Request(url, data = data, headers = headers)
# reponse = urllib2.urlopen(request)
# print(reponse.getcode())
#
# #3  下载网页方法3 ：添加特殊情景的处理器
# #创建cookie容器
# cookie = cookiejar.CookieJar()
# #创建一个opener
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# #给urllib2安装opener
# urllib2.install_opener(opener)
# reponse = urllib2.urlopen('http://www.baidu.com')
# print(reponse.getcode())