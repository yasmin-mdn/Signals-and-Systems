import array as arr
import numpy as np
import matplotlib.pyplot as plt

#initialize domain
n=arr.array('i',[])
for i in range(-50,51):
    n.append(i)

#making x[n]
x=arr.array('d',[])
for i in range(-50,51):
 x.append(2*np.exp(0.1*n[i+50]))

 #show
plt.stem(n,x,'c')
plt.show()
