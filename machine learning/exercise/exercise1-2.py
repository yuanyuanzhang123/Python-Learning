#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/25 22:02
# @Author  : Zhangyuanyuan
# @Site    : 
# @File    : exercise1-2.py
# @Software: PyCharm Community Edition

from numpy import *
from pandas import *
import matplotlib.pyplot as plt

# cost function
def ComputeCost(x,y,theta):
    m = len(x)
    return sum(power(((x*theta.T)-y),2))/(2*m)
#data = read_csv('ex1data1.csv')#直接这样读取，会将第一行的数当做列名，从而下面shape统计会少一行data
data = read_csv('ex1data1.csv',header=None,names=['Population','Profit'])
#print(data)
data.insert(0,'ones',1)
#print(data)
cols = data.shape[1]
x=data.iloc[:,0:cols-1]
y=data.iloc[:,cols-1:cols]
X=np.matrix(x.values)
Y=np.matrix(y.values)
theta=np.matrix(np.array([0,0]))
print(X.shape)#调试矩阵运算的时候可以通过打印shape来观察行列数
print(theta.shape)
print(theta)
print(Y.shape)
print(ComputeCost(X,Y,theta))#第一次设置初始theta后计算的cost function 为32.0727338775

#下面使用梯度下降算法不断调整theta，求最优解,即min(cost)
def gradientdescent(x,y,theta,alpha,maxloop):
    temp = np.matrix(np.zeros(theta.shape))# theta 初始化
    features = int(theta.ravel().shape[1]) # 获取特征个数
    cost = np.zeros(maxloop)  # 算法迭代次数

    for i in range(maxloop):
        error = (x * theta.T) - y
        for j in range(features):
            term = np.multiply(error,x[:,j])
            temp[0,j]=theta[0,j]-((alpha/len(x))*np.sum(term))

        theta = temp
        cost[i]=ComputeCost(x,y,theta)

    return theta,cost

alpha = 0.01
maxloop = 1000
thetas,costs = gradientdescent(X,Y,theta,alpha,maxloop)

print(thetas)
print(costs[maxloop-1])# 打印迭代1000次之后的cost结果，为4.51595550308，显然比第一次好很多

# 图形化cost function
x=np.linspace(data.Population.min(),data.Population.max(),100)
fun = thetas[0,0] + (thetas[0,1]*x)

fig,ax = plt.subplots(figsize=(12,8))
ax.plot(x,fun,'r',label='Prediction')
ax.scatter(data.Population,data.Profit,label='Training Data')
ax.legend(loc=2)
ax.set_xlabel('Population')
ax.set_ylabel('Profit')
ax.set_title('Predicted Profit vs. Populution Size')
plt.show()