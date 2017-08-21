#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/21 19:40
# @Author  : Zhangyuanyuan
# @Site    : 
# @File    : Day12.py
# @Software: PyCharm Community Edition

#从python学习公众号学习到的爬去股票信息的爬虫
#获取上交所和深交所所有股票的名称和交易信息
#从东方财富网获取股票列表，依次获取股票代码，增加到百度股票的链接中，对这些链接进行访问获取股票的信息
import  requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return  r.text
    except:
        return ""

def getStockList(lst,stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html,"html.parser")
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}",href)[0])
        except:
            continue

def getStockInfo(lst,stockURL,fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html,"html.parser")
            stockInfo = soup.find('div',attrs={'class':'stock-bets'})
            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称':name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(fpath,'a',encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count = count +1
                print('\r当前进度：{:.2f}%'.format(count*100/len(lst),end=""))

        except:
            count = count + 1
            print('\r当前进度：{:.2f}%'.format(count * 100 / len(lst), end=""))


def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = './stockinfo.txt'

    slist = []
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_info_url,output_file)

main()

