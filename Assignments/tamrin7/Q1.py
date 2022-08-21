import scipy as sc
import math
import numpy as np
import matplotlib.pyplot as plt
j=np.complex(0,1)
def a(X):
    N=len(X)
    a=[]
    t=[]
    for i in range(0,N):
        t.append(0)

    for k in range(0,N):
        for n in range(0,N):
            t[k]+=X[n]*np.exp((-1*j*2*np.pi*n*k)/N)
        a.append(t[k]*(1/N))
    return a

print(a([1,0.5,0.5]))
print("/////////////////////////////////")
print(a([1,0.5,0,0,0.5]))
print("/////////////////////////////////")
x=[0,0,0,0]
for n in range(0,4):
    x[n]=1+np.cos(2*np.pi*n)+np.sin(np.pi*n)+np.cos(np.pi*n/2)
print(a(x))

x=[0,1,2,3,4,5,4,3,2,1,0]
print(a(x))

