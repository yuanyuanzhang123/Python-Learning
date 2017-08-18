#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/17 19:50
# @Author  : Zhangyuanyuan
# @Site    : 
# @File    : Day9.py
# @Software: PyCharm Community Edition

import requests
from bs4 import BeautifulSoup as bs
import re
import pandas
import matplotlib.pyplot as plt
import  matplotlib
import numpy
import codecs
import jieba
matplotlib.rcParams['figure.figsize']=(10.0,5.0)
from wordcloud import WordCloud

#获取页面信息
def get_movie_html(url):
    response = requests.get(url)
    soup = bs(response.content,'html.parser')
    now_playing = soup.find_all('div',id='nowplaying')
   # print(now_playing[0])
    moive_list = now_playing[0].find_all('ul',class_= 'lists')
  #  print(moive_list)
    moive_detail = moive_list[0].find_all('li',class_='list-item')
   # print(a)
    now_playing_list=[]
    for item in moive_detail:
        data_list={}
        data_list['id']=item['id']
        data_list['name']=item['data-title']
        now_playing_list.append(data_list)
    return now_playing_list

def get_comments_by_id(id,page):
    comment_list=[]
    if page>0:
        start = (page-1)*20
    else:
        return False
    url = "https://movie.douban.com/subject/"+id+"/comments?start={}&limit=20".format(start)
    response = requests.get(url)
    soup = bs(response.content,"html.parser")
    comments = soup.find_all('div',class_='comment')
    for item in comments:
        if item.find_all('p')[0].string is not None:
            comment_list.append(item.find_all('p')[0].string)
    return comment_list





if __name__ == "__main__":
    start_url = "https://movie.douban.com/nowplaying/shanghai/"
    playing_list = get_movie_html(start_url)
    comments_l = []
    #获取前10页的短评内容
    for i in range(10):
        i = i+1
        comment_list = get_comments_by_id(playing_list[0]['id'],i)
        comments_l.append(comment_list)

     # 将列表中的数据转换为字符串
    comments = ''
    for k in range(len(comments_l)):
        comments = comments + (str(comments_l[k])).strip()

    # 使用正则表达式去除标点符号
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    filterdata = re.findall(pattern, comments)
    cleaned_comments = ''.join(filterdata)

    # 使用结巴分词进行中文分词
    segment = jieba.lcut(cleaned_comments)
    words_df = pandas.DataFrame({'segment': segment})

    # 去掉停用词
    stopwords = pandas.read_csv("stop_words_zh_UTF-8.txt", index_col=False, quoting=3, sep="\t", names=['stopword'],
                            encoding='utf-8')  # quoting=3全不引用
    words_df = words_df[~words_df.segment.isin(stopwords.stopword)]

    # 统计词频
    words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数": numpy.size})
    words_stat = words_stat.reset_index().sort_values(by=["计数"], ascending=False)


    word_frequence = {x[0]: x[1] for x in words_stat.head(1000).values}
    word_frequence_list = {}
    for key in word_frequence:
        word_frequence_list[key] = word_frequence[key]
   # print(word_frequence_list)

    # 用词云进行显示
    wordcloud = WordCloud(font_path="simhei.ttf", background_color="white", max_font_size=80).fit_words(word_frequence_list)#fit_words参数为dict类型

    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


