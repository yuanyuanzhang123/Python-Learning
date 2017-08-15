#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/15 20:00
# @Author  : Zhangyuanyuan
# @Site    : 
# @File    : Day6.py
# @Software: PyCharm Community Edition

import requests
import urllib
from bs4 import BeautifulSoup
import pdfkit

def parse_url_to_html(urls):
    files = []
    try:
        for index, url in enumerate(urls):
            response = requests.get(url)
            soup = BeautifulSoup(response.content,"html.parser")
            body = soup.find_all(class_="x-wiki-content")[0]#获取正文
            html = str(body)
            filename = "html/a_{}.html".format(index)
            with open(filename,'wb') as f:
                f.write(html.encode())
            files.append(filename)
    except:
        pass
    return files

def get_url_list():
    response = requests.get("https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000")
    soup = BeautifulSoup(response.content, "html.parser")
    menu_tag = soup.find_all(class_="uk-nav uk-nav-side")[1]#获取目录的内容链接
    urls = []
    for li in menu_tag.find_all("li"):
        url = "http://www.liaoxuefeng.com" + li.a.get('href')
        urls.append(url)
    return urls

def save(files):#html to pdf
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
        'outline-depth': 10
    }
    pdfkit.from_file(files,"Python.pdf",options=options)

if __name__ == "__main__":
    urls = get_url_list()

    files = parse_url_to_html(urls)

    save(files)



















