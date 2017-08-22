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



