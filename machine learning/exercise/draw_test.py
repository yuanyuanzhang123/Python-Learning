#!/usr/bin/env python

from numpy import *
from pandas import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
from matplotlib import cm

def ComputeCost(x,y,theta):
    m = len(x)
    return sum(power(((x*theta.T)-y),2))/(2*m)

def gradientdescent(x,y,theta,alpha,maxloop):
    thetas={}
    temp = np.matrix(np.zeros(theta.shape))# theta 初始化
    features = int(theta.ravel().shape[1]) # 获取特征个数
    cost = np.zeros(maxloop)  # 算法迭代次数

    for j in range(features): # 初始化字典
        thetas[j] = [theta[0,j]]

    for i in range(maxloop):
        error = (x * theta.T) - y
        for j in range(features):
            term = np.multiply(error,x[:,j])
            temp[0,j]=theta[0,j]-((alpha/len(x))*np.sum(term))
            thetas[j].append(temp[0,j])

        cost[i]=ComputeCost(x,y,theta)

    return thetas,cost

#
def draw_3d(thetas):
    size = 100
    theta0Vals = np.linspace(-10,10, size)
    theta1Vals = np.linspace(-2, 4, size)
    JVals = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            col = np.matrix([theta0Vals[i], theta1Vals[j]])
            JVals[i,j] = ComputeCost(X,Y,col)

    theta0Vals, theta1Vals = np.meshgrid(theta0Vals, theta1Vals)
    JVals = JVals.T
    # 绘制能量下降曲面
    fig = plt.figure()
    #ax = fig.gca(projection='3d') # matlablib version 0.99
    ax = Axes3D(fig) # matlablib version 1.0

    ax.plot_surface(theta0Vals, theta1Vals, JVals,  rstride=2, cstride=2, alpha=0.3,
                cmap=cm.rainbow, linewidth=0, antialiased=False)
    ax.plot(thetas[0], thetas[1], 'rx', markersize=3, linewidth=1)
  #  ax.plot([0], thetas[1], 'r-')
    ax.set_xlabel(r'$\theta_0$')
    ax.set_ylabel(r'$\theta_1$')
    ax.set_zlabel(r'$J(\theta)$')
    plt.show()

    # 绘制能量轮廓
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set_xlabel(r'$\theta_0$')
    ax.set_ylabel(r'$\theta_1$')

    CS = ax.contour(theta0Vals, theta1Vals, JVals, np.logspace(-2, 3, 20))
    plt.clabel(CS, inline=1, fontsize=10)
   # ax.plot(thetas[0, 0], thetas[1, 0], 'rx', markersize=10, linewidth=2)

    plt.show()

if __name__ == "__main__":
    data = read_csv('ex1data1.csv', header=None, names=['Population', 'Profit'])
    # print(data)
    data.insert(0, 'ones', 1)
    cols = data.shape[1]
    x = data.iloc[:, 0:cols - 1]
    y = data.iloc[:, cols - 1:cols]
    X = np.matrix(x.values)
    Y = np.matrix(y.values)
    theta = np.matrix(np.array([0, 0]))
    alpha = 0.01  # learning rate
    maxloop = 1000
    thetas, costs = gradientdescent(X, Y, theta, alpha, maxloop)
    draw_3d(thetas)
