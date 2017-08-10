#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/10 18:44
# @Author  : Zhangyuanyuan
# @Site    : 
# @File    : Day1.py
# @Software: PyCharm Community Edition

import time
from multiprocessing.dummy import Pool as ThreadPool
import sys
import requests
from lxml import etree
import json
import pymongo

def get_resopnse(url):
    html = requests.get(url,headers = headers)
    selector = etree.HTML(html.text)
    product_list = selector.xpath('//*[@id="J_goodsList"]/ul/li')
    for product in product_list:
        try:
            sku_id = product.xpath('@data-sku')[0]
            product_url = 'https://item.jd.com/{}.html'.format(str(sku_id))
           # print(product_url)
            get_product(product_url)
        except Exception as e:
            print(e)

def get_product(product_url):
    product_dict = {}
    html = requests.get(product_url,headers = headers)
    selector = etree.HTML(html.text)
    product_infos = selector.xpath('//ul[@class="parameter2 p-parameter-list"]')
    for product in product_infos:
        product_number = product.xpath('li[2]/@title')[0]
        product_price = get_product_price(product_number)
        product_dict['商品编号'] = product_number
        product_dict['商品价格'] = product_price
        product_dict['商品名称'] = product.xpath('li[1]/@title')[0]
    for items in product_dict.values():
        print(items)
    save_data(product_dict)

def get_product_price(sku):
    """
    获取价格
    :param sku:
    :return:
    """
    price_url = 'https://p.3.cn/prices/mgets?&skuIds=J_{}'.format(str(sku))
    response = requests.get(price_url,headers=headers).content
    response_json = json.loads(response)
    for info in response_json:
        return info.get('p')

def save_data(product_list):
    pass

if __name__ == "__main__":
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3178.0 Safari/537.36"
    }
    urls = ["https://search.jd.com/Search?keyword=手机&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&suggest=1.def.0.V07&wq=shouji&cid2=653&cid3=655&page={}&s=1&click=0".format(page) for page in range(1,10,2)]
    start_time = time.time()
    pool = ThreadPool(2)
    pool.map(get_resopnse,urls)
    pool.close()
    pool.join()
    end_time = time.time()
    print("用时",str(end_time - start_time),"秒")

