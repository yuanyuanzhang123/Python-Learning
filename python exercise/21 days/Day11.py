#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/20 21:59
# @Author  : Zhangyuanyuan
# @Site    : 
# @File    : Day11.py
# @Software: PyCharm Community Edition

import requests
import urllib
from lxml import etree
import  codecs
import json

def GetTimeByArticle(url):
    try:
        response = requests.get(url)
        selector = etree.HTML(response.text)
        time_text = selector.xpath('//div[@class="n_post_time"]')[1].text
        return time_text
    except:
        pass
if __name__ == "__main__":
    out_file = codecs.open('tieba.json','w',encoding='utf-8')
    for pn in range(0,250,50):
        kw = u'网络爬虫'.encode('utf-8')
        url = 'http://tieba.baidu.com/f?kw=网络爬虫'+'&ie=utf-8&pn='+str(pn)
        response = requests.get(url)
       # html = response.read()
       # print(response.text)

        html_dom=etree.HTML(response.text)
        for site in html_dom.xpath('//li[@class=" j_thread_list clearfix"]'):
            text_title = site.xpath('.//a/@title')
            title = site.xpath('.//span/@title')[1]#第一个span标签下的title属性
            #site.xpath('.//a')返回的是一个list，取这个list的第一个值获取其属性href的内容
            article_url = site.xpath('.//a')[1].attrib['href']
            reply_date=GetTimeByArticle('http://tieba.baidu.com'+article_url)


            items = {}
            items['title'] = text_title
            items['author']= title
          #  items['lastName']=lastName
            items['reply_date']=reply_date
            print(items)

            line = json.dumps(items,ensure_ascii=False)
           # print(line)
            out_file.write(line+"\n")
        out_file.close()
    print("end")































