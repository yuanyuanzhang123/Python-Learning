#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/22 19:02
# @Author  : Zhangyuanyuan
# @Site    : 
# @File    : Day13.py
# @Software: PyCharm Community Edition

#K邻近算法
import numpy as np
import operator
import matplotlib
import matplotlib.pyplot as plt

def createDataSet():
    group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def classifg_k(inX,dataSet,labels,K):
    dataSetSize = dataSet.shape[0]
    #计算两个向量点之间的距离
    diffMat = np.tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances**0.5
    sortedDistIndices = distances.argsort()
    classCount = {}
    # 选择距离最小的K个点
    for i in range(K):
        votelabel = labels[sortedDistIndices[i]]
        classCount[votelabel] = classCount.get(votelabel,0) + 1
    sortedClassCount = sorted(classCount.items(),key = operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

features,labels = createDataSet()
print(classifg_k([0,0],features,labels,3))

def file2matrix(filename):
    with open(filename,'r') as f:
        #获取文件行数
        arrayLines = f.readlines()
        arrayLen = len(arrayLines)
        #创建存储文件数据的numpy矩阵
        returnMat = np.zeros((arrayLen,3))
        LabelVector = []
        index = 0
        #解析文件数据到列表
        for line in arrayLines:
            line = line.strip()
            listFromLine = line.split('\t')
            returnMat[index,:] = listFromLine[0:3]
            LabelVector.append(int(listFromLine[-1]))
            index += 1
    f.close()
    return returnMat,LabelVector

def draw_k(features,labels):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(features[:,1],features[:,2],15.0*np.array(labels),15.0*np.array(labels))
    plt.show()


def autoNorm(dataSet):
    minvals = dataSet.min(0)  # 从列中选取最小值
    maxVals = dataSet.max(0)
    ranges = maxVals - minvals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minvals, (m, 1))
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    return normDataSet, ranges, minvals


def datingClasTest():
    h = 0.10
    features,labels = file2matrix("datingTestSet2.txt")
    normMat,ranges,minVals = autoNorm(features)
    m = normMat.shape[0]
    testVecs = int(m*h)
    error = 0.0
    for i in range(testVecs):
        classiferResult = classifg_k(normMat[i,:],normMat[testVecs:m,:],labels[testVecs:m],3)
        print("classifer came back with:%d, the real answer is: %d" % (classiferResult,labels[i]))
        if (classiferResult != labels[i]):
            error += 1.0
    print("total error rate is %f" %(error/float(testVecs)))

if __name__ == "__main__":
    #filename = "datingTestSet2.txt"
   # features,labels = file2matrix(filename)
  #  draw_k(features,labels)
    datingClasTest()

