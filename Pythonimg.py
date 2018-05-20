#coding=utf-8
import urllib.request
import re

def getHtml(url):
	#page=urllib.request.urlopen(url)#获取网页内容，Python3的用法
	req=urllib.request.Request(url,headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
})
	page=urllib.request.urlopen(req)
	html=page.read()
	return html.decode('UTF-8')


def getJpg(html):
	reg=r'src="(.+?\.jpg)" pic_ext'
	imgre=re.compile(reg)
	imglist=re.findall(imgre,html)
	return imglist

html=getHtml("http://blog.csdn.net/mr_tank_/article/details/14102159")
print(html)
print(getJpg(html))