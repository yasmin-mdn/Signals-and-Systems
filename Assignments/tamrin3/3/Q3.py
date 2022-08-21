import matplotlib.pyplot as plt
import numpy as np
import array as arr
from numpy import ndarray

def convolution(x,h) :
  m=len(x)
  n=len(h)
  X=arr.array('d',[])
  H=arr.array('d',[])
 

  Y = ndarray((m+n-1,))

  X= x
  H= h
  for i in range(0,m+n):
    Y[i]=0
    for j in range(0,m):
      if i-j+1>0:
        Y[i]=Y[i]+X[j]*H[i-j+1]
  return Y
t=[]
h=[1,1,1,1]
x=-1*np.ones(50)
t=convolution(x,h)
plt.stem(t)
plt.show()