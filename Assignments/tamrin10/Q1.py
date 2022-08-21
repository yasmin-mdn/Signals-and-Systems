import numpy as np
import matplotlib.pyplot as plt
T=1
pi=np.pi
s1= -1*(np.exp(2*pi/T))
m1=(1-np.exp(2*pi/T))

s2=1
m2=(1-np.exp(-1*2*pi/T))
result=1/T*(s1/m1+s2/m2)

plt.stem(result)
plt.show()
