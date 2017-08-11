#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/11 18:13
# @Author  : Zhangyuanyuan
# @Site    : 
# @File    : Day2.py
# @Software: PyCharm Community Edition

import urllib.request,re
import urllib

def get_data():
    html = urllib.request.urlopen(url)
    content = html.read().decode('utf-8')#重点在这，获取到的网页需要再转换成utf-8格式
    reg = re.compile('<a class="name list-right" href="(.*?)" target="_blank" .*?>(.*?)</a>',re.S)

    items = re.findall(reg,str(content))
    print(len(items))
    file = open('data.txt','w')
    file.write(str(items))
    file.close()
    for i in items:
        print("网址： "+i[0]+"  小说名称： "+ i[1])

if __name__ == "__main__":
    url = "http://r.qidian.com/mm"
    get_data()