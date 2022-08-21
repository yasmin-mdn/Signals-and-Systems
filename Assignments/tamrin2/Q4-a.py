import array as arr
import numpy as np
import matplotlib.pyplot as plt

#moving axis to center
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

#const variables
w=np.pi/3
t=np.pi/4


#initialize domain
n = arr.array('i',[])
for i in range(-50,51):
    n.append(i)

#making x[n]
x= arr.array('d',[])
for i in range(-50,51):
 x.append(np.cos(w*n[i+50]+t))

 #show
plt.stem(n,x,'g')
plt.show()