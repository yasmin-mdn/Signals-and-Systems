import scipy as sc
import numpy as np 
import matplotlib.pyplot as plt

#Q5 b
x = np.cos(np.linspace(0,4.*np.pi,100))
y1 = sc.convolve(np.ones(5), x) 
y2 = sc.convolve([1, -1, -1, -1, 1], x) 
y = sc.convolve(np.ones(3), y1+y2)
plt.stem(y)
plt.show()
h=sc.convolve([2,0,0,0,2],np.ones(3))
y=sc.convolve(h,x)
plt.stem(y)
plt.show()

#Q5 c

x=np.ones(100)
y1 = sc.convolve(np.ones(5), x) 
y2 = sc.convolve([1, -1, -1, -1, 1], x) 
y = sc.convolve(np.ones(3), y1+y2)
plt.stem(y)
plt.show()
h=sc.convolve([2,0,0,0,2],np.ones(3))
y=sc.convolve(h,x)
plt.stem(y)
plt.show()