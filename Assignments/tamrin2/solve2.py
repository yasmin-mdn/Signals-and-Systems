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


x = np.linspace(0.1, 2 * np.pi, 45)
y = np.exp(np.sin(x))
plt.stem(x, y, use_line_collection=True)
plt.show()