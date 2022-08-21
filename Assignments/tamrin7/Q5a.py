import scipy as sc
import math
import numpy as np
import matplotlib.pyplot as plt
x=[]
def fill_x(n):
    if n>=0 and n<=5:
        x.append(n)
    elif n>5 and n<=10:
        x.append(10-n)
    else:
        x.append(0)
    return x
N=10000
n=np.arange(N) 
#n=np.linspace(0,2*np.pi,10000)
for t in n:
    x=fill_x(t)


f=np.fft.fft(x)

plt.figure()
plt.subplot(1, 3, 1)
plt.plot(f)
plt.subplot(1, 3, 2)
plt.plot(np.abs(f))
plt.subplot(1, 3, 3)
plt.plot(np.angle(f))
plt.show()

