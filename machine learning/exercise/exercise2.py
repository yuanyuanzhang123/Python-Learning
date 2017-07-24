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
from sklearn import linear_model

def ComputeCost(x,y,theta):
    m = len(x)
    return sum(power(((x*theta.T)-y),2))/(2*m)

def gradientDescent(x,y,theta,alpha,loops):
    temp = np.matrix(np.zeros(theta.shape))
    para = int(theta.ravel().shape[1])
    cost = np.zeros(loops)

    for i in range(loops):
        error = (x * theta.T) - y
        for j in range(para):
            term = np.multiply(error,x[:,j])
            temp[0,j] = theta[0,j] - ((alpha/len(x))*np.sum(term))

        theta = temp
        cost[i] = ComputeCost(x,y,theta)
    return theta,cost

def draw_cost(loops,costs):
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(np.arange(loops),costs,'r')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Cost')
    ax.set_title('Error vs. Training Epoch')
    plt.show()

def sklearn_linear_fun(x,y):
    model = linear_model.LinearRegression()
    model.fit(x,y)

if __name__ == "__main__":
    #intialize data
    data2 = read_csv('ex1data2.csv', header=None, names=['Size', 'Bedrooms', 'Price'])
   # print(data2.head())
    data2 = (data2 - data2.mean()) / data2.std()  # normalization
   # print(data2.head())
    theta = np.matrix(np.array([0,0,0]))
    #print(theta)
    data2.insert(0,"ones",1)
    cols=data2.shape[1]
    x2 = data2.iloc[:,0:cols-1]
    y2 = data2.iloc[:,cols-1:cols]
    x2 = matrix(x2.values)
    y2 = matrix(y2.values)
    alpha = 0.05
    loops = 1000
    # call fun
    thetas,costs = gradientDescent(x2,y2,theta,alpha,loops)
    print(ComputeCost(x2,y2,thetas))
    draw_cost(loops,costs)