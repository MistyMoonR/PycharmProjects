from numpy import *
import numpy as np

import scipy

data2=mat(ones((3,3)))

data3=[1,2,3]

data6=mat(eye(2,2,dtype=int))

A=mat([[1,0,0],[2,1,0],[0,0,1]])
B=mat([[1,3,0],[0,1,0],[0,0,1]])
C=mat([[1,0,-1,2],[2,3,1,2],[1,-1,2,1]])
print(A)
print(B)
print(C)

d = np.linalg.det(A)
print(d)
import numpy
#e = np.linalg.inv(A)

print(data2)
print(data3)
print(data6)

print(A.T)
print(A**-1)

#