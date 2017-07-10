#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/9 9:15
# @Author  : Zhangyuanyuan
# @Site    : 
# @File    : numpy-learn.py
# @Software: PyCharm Community Edition

import numpy as np

print(np.__version__)
#print(np.show_config())

#create a null vector
z = np.zeros(10)
print(z)# [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]

# get the documentation of the numpy add function
# in command line usage---python -c "import numpy;numpy.info(numpy.add)"
print(np.info(np.add))

# set the fifth value which is 1
z[4] = 1
# Create a vector with values ranging from 10 to 49
z=np.arange(10,50)
print(z)
"""
output:
[10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34
 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49]
"""
# reverse a vector
z = z[::-1]
print(z)
"""
output:
[49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25
 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10]
"""
#Create a 3x3 matrix with values ranging from 0 to 8
z = np.arange(0,9).reshape(3,3)
print(z)
"""
output:
[[0 1 2]
 [3 4 5]
 [6 7 8]]
"""
z = np.eye(3)#  identity matrix
print(z)

# Create a 3x3x3 array with random values
z = np.random.random((3,3,3))
print(z)

zmin,zmax = z.min(),z.max()
print(zmin,zmax)

zmean = z.mean()
print(zmean)

# Create a 2d array with 1 on the border and 0 inside
z = np.ones((10,10))
z[1:-1,1:-1] = 0
print(z)
"""
output :
[[ 1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  1.]
 [ 1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]]
"""

print(0*np.nan) # nan
print(np.nan==np.nan) # False
print(np.inf>np.nan) # False
print(np.nan - np.nan)# nan
print(0.3 == 3*0.1)# False

# Create a 5x5 matrix with values 1,2,3,4 just below the diagonal
Z = np.diag(1+np.arange(4),k=-1)
print(Z)
"""
output :
[[0 0 0 0 0]
 [1 0 0 0 0]
 [0 2 0 0 0]
 [0 0 3 0 0]
 [0 0 0 4 0]]
"""
# Create a 8x8 matrix and fill it with a checkerboard pattern
Z = np.zeros((8,8),dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)
"""
output :
[[0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]]
"""
# Create a checkerboard 8x8 matrix using the tile function
Z = np.tile( np.array([[0,1],[1,0]]), (4,4))
print(Z) # same as last one

# Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element
print(np.unravel_index(100,(6,7,8))) #(1, 5, 4)

# Normalize a 5x5 random matrix
Z = np.random.random((5,5))
Zmax, Zmin = Z.max(), Z.min()
Z = (Z - Zmin)/(Zmax - Zmin)
print(Z)
"""
output :
[[ 0.23879039  0.68182217  0.52051684  0.45361351  0.25473306]
 [ 0.18907368  0.9967811   0.41514393  0.87159143  0.67242616]
 [ 0.57016219  0.61484117  0.45151348  0.22795414  0.46224294]
 [ 0.63487098  0.4646382   1.          0.93618741  0.65204104]
 [ 0.96565681  0.43844611  0.          0.28426401  0.81801136]]
"""