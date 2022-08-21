import numpy as np
import scipy as sc
import math
import matplotlib.pyplot as plt
n=np.arange(-200,201,1)

#0<|w|<pi/8
h1=[]
for i in n:
    h1.append(np.sin((np.pi/8)*i)/(np.pi*i))
#plt.stem(n,h1)
#plt.show()

#3*pi/8<|w|<5*pi/8
h2=[]
for i in n:
    h2.append(2/3*((np.sin((3*np.pi/8)*i)/(np.pi*i))+(np.sin((5*np.pi/8)*i)/(np.pi*i))))
#plt.stem(n,h2)
#plt.show()


#7*pi/8<|w|<pi
h3=[]
for i in n:
    h3.append(1/3*((np.sin((7*np.pi/8)*i)/(np.pi*i))+(np.sin(np.pi*i)/(np.pi*i))))
#plt.stem(n,h3)
#plt.show()


plt.figure()
plt.subplot(3, 1, 1)
plt.stem(n,h1)
plt.subplot(3, 1, 2)
plt.plot(n,h2)
plt.subplot(3, 1, 3)
plt.plot(n,h3)
plt.show()