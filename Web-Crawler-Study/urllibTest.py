#! /usr/python/
# -*- coding: UTF-8 -*-

import cookielib
import urllib2

url = "http://www.baidu.com"
response1 = urllib2.urlopen(url)
print ("First Methond")
# get State Code,200 is Successed
print response1.getcode()
# get web length
print len(response1.read())

print("第二种方法")
request = urllib2.Request(url)
# 模拟Mozilla浏览器进行爬虫
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

print("第三种方法")
cookie = cookielib.CookieJar()
# 加入urllib2处理cookie的能力
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
print len(response3.read())
print cookie
