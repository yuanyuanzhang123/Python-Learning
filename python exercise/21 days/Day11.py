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
    response = requests.get(url)
    selector = etree.HTML(response.text)
    print(response.text)
    time_text = selector.xpath('//div[@class="n_post_time"]')[1].text
    return time_text

if __name__ == "__main__":
    out_file = codecs.open('tieba.json','w',encoding='utf-8')
    for pn in range(0,250,50):
        kw = u'网络爬虫'.encode('utf-8')
        url = 'http://tieba.baidu.com/f?kw=网络爬虫'+'&ie=utf-8&pn='+str(pn)
        print(url)
        response = requests.get(url)
       # html = response.read()
       # print(response.text)

        html_dom=etree.HTML(response.text)
        for site in html_dom.xpath('//div[@class="threadlist_author pull_right"]'):
           # print(site)
            title = site.xpath('.//a')[0].text
            article_url = site.xpath('.//a')[0].attrib['href']
            print(article_url)
         #   reply_date=GetTimeByArticle('http://tieba.baidu.com'+article_url)

            introduce = site.xpath('.//*[@class="threadlist_abs threadlist_abs_onlyline "]')[0].text.strip()
            author = site.xpath('.//*[@class="frs-author-name j_user_card "]')[0].text.strip()
            lastName = site.xpath('.//*[@class="frs-author-name j_user_card "]')[1].text.strip()
            print(title, introduce, article_url, author, lastName)

            items = {}
            items['title'] = title
            items['author']=author
            items['lastName']=lastName
           # items['reply_date']=reply_date
            print(items)

            line = json.dumps(items,ensure_ascii=False)
            print(line)
            out_file.write(line+"\n")
        out_file.close()
    print("end")































