import numpy as np 
import matplotlib.pyplot as plt 
#import scipy as sc 
x1=[]
x2=[]
n=[0,1,2,3,4,5,6,7,8,9,10,11,12]
h=np.ones(13)

for i in n:
    x2.append(np.heaviside(i-1,1)-2*np.heaviside(i-4,1)+np.heaviside(i-7,1))
y2=np.convolve(h,x2,'full')
plt.stem(y2)
plt.show()




for i in n:
    x1.append((np.heaviside(i,1)-np.heaviside(i-12,1))*np.sin((np.pi/6)*i))
y1=np.convolve(h,x1,'full')
plt.stem(y1)
plt.show()



