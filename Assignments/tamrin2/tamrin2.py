import scipy
import numpy as np
import matplotlib.pyplot as plt

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
w=np.pi/3
t=np.pi/4
n = np.linspace(-50, 50,10)
x=np.cos(w*n+t)
plt.stem(n,x)
#plt.plot(x,scalex=True,scaley=True)
plt.show()