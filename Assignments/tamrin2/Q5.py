import numpy as np
import matplotlib.pyplot as plt
import array as arr


n = arr.array('i',[])
for i in range(-5,6):
    n.append(i)
    


x = arr.array('d',[])
for i in range(-5,6):
 x.append(3*np.sin(np.pi*n[i+5])+(3*np.abs(np.cos(7*n[i+5]))))

plt.stem(n,x,'c')
plt.show()

#limit the signal
for i in range(-5,6):
  if x[i+5]>5:
    x[i+5]=5
  elif x[i+5]<0:
    x[i+5]=0

plt.stem(n,x,'r')
plt.show()


