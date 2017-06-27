#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/22 21:22
# @Author  : Zhangyuanyuan
# @Site    : 
# @File    : exercise1.py
# @Software: PyCharm Community Edition

from numpy import *
from pandas import *
import matplotlib.pyplot as plt
# 1
print(eye(5,dtype=int))
# 2 绘制散列图
data = read_csv('ex1data1.csv')
#print(data.values)
data2 = mat(data)# 如果不转化为矩阵，这里data是一个list不支持hash操作，即下面的获取x和y
x = data2[:,0]
y = data2[:,1]
ax = plt.plot(x,y,'ob')# 'ob'代表散列图
plt.setp(ax,color='r') # 设置颜色为红色，默认为蓝色
plt.ylabel('Population of City in 10,000s')
plt.xlabel('Profit in $10,000s')
plt.show()
print(x)
#print(dir(data))

# 绘制散列函数第二种方式
path = 'ex1data1.csv'
data_a = read_csv(path ,header = None,names=['Population of City in 10,000s','Profit in $10,000s'])# 加上列名
print(data_a)
data_a.plot(kind = 'scatter',x = 'Population of City in 10,000s',y = 'Profit in $10,000s',color = 'r')
plt.show()

