#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/16 19:40
# @Author  : Zhangyuanyuan
# @Site    : 
# @File    : Day7.py
# @Software: PyCharm Community Edition

import os
import re
import time
import urllib
from bs4 import BeautifulSoup
import pdfkit
import requests

class CrawlerPDF(object):
    """
    爬虫基类
    """
    name = None
    def __init__(self,name,start_url):
        """
        初始化
        :param name: 将要保存的pdf文件名
        :param start_url: 爬虫入口url
        """
        self.name = name
        self.start_url = start_url
       # self.domain = '{uri.scheme}://{uri.netloc}'.format(uri=urllib.parse(self.start_url))
        self.domain = "http://nbviewer.jupyter.org"


    @staticmethod
    def get_response(url,**headers):
        """
        网络请求，返回response对象
        :param url:
        :param args:
        :return:
        """
        response = requests.get(url,**headers)
        return response

    def parse_menu(self,response):
        """
        从response中解析出所有目录的URL链接，由子类实现
        :param response:
        :return:
        """
        raise NotImplementedError

    def parse_body(self,response):
        """
        解析正文,由子类实现
        :param response: 爬虫返回的response对象
        :return: 返回经过处理的html正文文本
        """
        raise NotImplementedError

    def genpdf(self,files):
        start_time = time.time()
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
            'outline-depth': 10,
        }
        pdfkit.from_file(files,self.name+".pdf",options=options)
        for file_n in files:
            os.remove(file_n)
        cost_time = time.time() - start_time
        print(u"总共耗时： %f 秒" % cost_time)

class MyCrawler(CrawlerPDF):
    """
    爬起Python Jupter NoteBook
    """

    def parse_menu(self, text_links):
        """
        下载正文
        :param response:
        :return:
        """
        file_names=[]
        for index, url in enumerate(text_links):
            html = self.parse_body(self.get_response(url))
            file_name =  "python/a_{}.html".format(index)
            with open(file_name, 'wb') as f:
                f.write(html.encode())
            file_names.append(file_name)
        return file_names



    def parse_body(self, response):
        """
        解析正文,由子类实现
        :param response: 爬虫返回的response对象
        :return: 返回经过处理的html正文文本
        """
        try:
            soup = BeautifulSoup(response.content,"html.parser")
            body = soup.find_all(class_ = "container container-main")[0]
            html = str(body)
            return html
        except:
            print("except")

    def parse_upper(self,links,reg_name):
        """
        从response中解析出所有目录的URL链接，由子类实现，可循环获取
        :param response:
        :return:
        """
        urls = []
        for index, url in enumerate(links):
            soup = BeautifulSoup((self.get_response(url)).content, "html.parser")
            menu_tag = soup.find_all(class_="table table-striped table-nbviewer")[0]
            for a_tag in menu_tag.find_all("a"):
                url = "http://nbviewer.jupyter.org" + a_tag.get('href')
                reg = re.compile(reg_name)
                result = reg.match(url)
                if result is not None:
                    if not url.startswith("http"):
                        url = ".".join([self.domain, url])
                    urls.append(url)
        return urls

if __name__ == "__main__":
    start_url = ["http://nbviewer.jupyter.org/github/lijin-THU/notes-python/tree/master/"]
    #测试本网址能否访问成功
    #headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3178.0 Safari/537.36"}
   # rep = requests.get(start_url,headers=headers)

    crawler = MyCrawler("jupyter notebook",start_url)
    urls = crawler.parse_upper(start_url,'.*?github/lijin-THU/notes-python/tree/master.*?')#顶层目录
    menu_urls = crawler.parse_upper(urls,'.*?github/lijin-THU/notes-python/blob/master.*?')#第二层目录
    files = crawler.parse_menu(menu_urls)#解析并下载正文

    crawler.genpdf(files)

















