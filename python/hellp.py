import numpy as np
from numpy import*

A = mat([[2, 1, -5], [3, 2, 4], [1, 0, 3]])


print("detA=",np.linalg.det(A))


for i in range(0,3):
    for j in range(0,3):
        aij=np.delete(np.delete(A,i,0),j,1)
        print("a%d%d=\n"%(i+1,j+1,),aij)
        print("",end="")
        ij=(-1)**(i+j)*np.linalg.det(aij)
        print("det%d%d="%(i+1,j+1),ij)
        det11 = 6.0
        det12 = -5.0
        det13 = -2.0
        det21 = -3.0
        det22 = 11.0
        det23 = 1.0
        det31 = 14.0
        det32 = -23.0
        det33 = 1.0
b=mat([[det11,det12,det13],[det21,det22,det23],[det31,det32,det33]]) #上面输出再输入
print(b.T)
print(A.I)

A=mat([[1,0,0],[2,1,0],[0,0,1]])
B=mat([[1,3,0],[0,1,0],[0,0,1]])
C=mat([[1,0,-1,2],[2,3,1,2],[1,-1,2,1]])
