import scipy as sc
import math
import numpy as np
import matplotlib.pyplot as plt
import random


def a(k):
    c=(1/(k*np.pi))*(np.cos(np.pi*(2/3)*k)-np.cos(np.pi*(1/3)*k))
    return c

#image of exp function
def mkImage(n,k):
    temp=np.sin(k*n*np.pi/3)
    return temp
#M=1
#M=2
#M=5
#M=10
M=50
arr=[]

x=[]
for i in range(2*M+1):
    arr.append(0)

for i in range(0,2*M+1):
    x.append((1/16)*i-4)
    n=(1/16)*i-4
    for k in range(1,M): 
        arr[i]+=a(k)*mkImage(n,k)
    for k in range(-M,0): 
        arr[i]+=a(k)*mkImage(n,k)

   

plt.plot(x,arr)
plt.show()
