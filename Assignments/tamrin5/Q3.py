from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import scipy
b=[1,0.8,0.64]
a=[1]
y=[]
n=np.arange(-4,20)


#impulse
x=signal.unit_impulse(24,5)
y=signal.lfilter(b,a,x)
plt.stem(n,y)
plt.show()


#step
x=np.heaviside(n,0)
y=signal.lfilter(b,a,x)
plt.stem(n,y)
plt.show()

