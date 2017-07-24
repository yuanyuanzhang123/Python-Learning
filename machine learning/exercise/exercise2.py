#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/21 15:41
# @Author  : Zyy
# @Site    : 
# @File    : exercise2.py
# @Software: PyCharm Community Edition

from numpy import *
from pandas import *
import matplotlib.pyplot as plt

data2 = read_csv('ex1data2.csv',header=None,names=['Size','Bedrooms','Price'])
print(data2.head())
data2 = (data2 - data2.mean())/data2.std()# normalization
print(data2.head())

def ComputeCost(x,y,theta):
    m = len(x)
    return sum(power(((x*theta.T)-y),2))/(2*m)

def gradientDescent(x,y,theta,alpha,loops):
    temp = np.matrix(np.zeros(theta.shape))
    para = int(theta.reval().shape[1])
    cost = np.zeros(loops)

    for i in range(loops):
        error = (x * theta.T) - y
        for j in range(para):
            term = np.multiply(error,x[:,j])
            temp[0,j] = theta[0,j] - ((alpha/len(x))*np.sum(term))

        theta = temp
        cost[i] = ComputeCost(x,y,theta)
    return theta,cost

theta = np.matrix(np.array([0,0,0]))
print(theta)
para = int(theta.reval().shape[1])
print(para)