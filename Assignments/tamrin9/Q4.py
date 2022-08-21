import numpy as np
import scipy as sc
import math
import matplotlib.pyplot as plt
x=[1,2,3,4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4]
h1=[2,-1,1,3,6,3,1,-1,2]
y1=np.convolve(x,h1,'full')

h2=[1,0.5,0.25,0.125,0.0625]
y2=np.convolve(x,h2,'full')

Y=[]
H=5*np.exp(np.complex(0,1)*np.pi/4)
X=np.fft.fft(x)
for i in range(0,len(X)):
    Y.append(X[i]*H)

y3=np.fft.ifft(Y)



plt.figure()
plt.subplot(4, 1, 1)
plt.plot(x)
plt.subplot(4, 1, 2)
plt.stem(y1)
plt.subplot(4, 1, 3)
plt.plot(y2)
plt.subplot(4, 1, 4)
plt.plot(y3)
plt.show()