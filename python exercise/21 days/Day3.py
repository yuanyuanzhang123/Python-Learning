#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/12 22:53
# @Author  : Zhangyuanyuan
# @Site    : 
# @File    : Day3.py
# @Software: PyCharm Community Edition

from bs4 import BeautifulSoup
import requests
import urllib

def crawl(url):
    # html = urllib.request.urlopen(url,headers = headers)
    html = requests.get(url,headers=headers)
    content = html.text
   # print(content)
    soup = BeautifulSoup(content,'html.parser')
    # <img width="170" src="https://img1.doubanio.com/view/photo/lthumb/public/p2329689629.webp" />
    pics = soup.find_all('img')
    x = 0
    for pic in pics:
        link = pic.get('src')
        print(link)
        urllib.request.urlretrieve(link,'image\{}.jpg'.format(x))
        x+=1

if __name__ == "__main__":
  #  ht = '<a href="http://www.baidu.com"></a>'
   # soup = BeautifulSoup(ht, 'html.parser')
   # a = soup.find_all('a')
    #for b in a:
    #    li = b.get('href')
   #     print(li)
    url = "https://www.douban.com/photos/album/1626714239/?from=tag"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3178.0 Safari/537.36"}
    crawl(url)