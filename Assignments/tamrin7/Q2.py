import scipy as sc
import math
import numpy as np
import matplotlib.pyplot as plt
x=[]
j=np.complex(0,1)

def make_x(n_range):
    for n in n_range:
        if n>=-5 and n<=5:
            x.append(1)
        elif (n>=-10 and n<-5) or (n>5 and n<=10):
            x.append(0)
    return x
#zarayeb
def a(k):
        t=0
        for n in range(0,N):
            t+=x[n]*np.exp((-1*j*2*np.pi*n*k)/N)
        return t


def estimate_signal(c,n_range):
    result = 0
    xn = []
    N=len(x)
    for n in n_range:
        result = 0
        for k in range(0, len(c)):
            result += c[k] *np.exp( j *k* 2 * np.pi *n/ N)
        xn.append(result)
    return xn


#Q2
x=[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0]

#ii
#x=[1,0.5,0.5]

#iii
#x=[1,0.5,0,0,0.5]

#iv
#x=[0,0,0,0]
#for n in range(0,4):
#    x[n]=1+np.cos(2*np.pi*n)+np.sin(np.pi*n)+np.cos(np.pi*n/2)

N=len(x)
M=range(0, N)
n_range=range(0,N)
plt.stem(n_range,x)
plt.show()
fig, axs = plt.subplots(int(N/2), 1, constrained_layout=True)
fig2,axs2=plt.subplots(int(N/2), 1, constrained_layout=True)

for m in M:
    c = []
    K = range(-m, m + 1)
    for k in K:
        c.append(a(k))
        xn = estimate_signal(c,n_range)
    if m>=0 and m<int(N/2):
        axs[M.index(m)-1 ].stem(n_range, xn)
        axs[M.index(m)-1 ].set_title('m = ' + str(m))
    else:
        axs2[N-M.index(m)-1].stem(n_range, xn)
        axs2[N-M.index(m)-1].set_title('m = ' + str(m))
    #plt.stem(n_range,xn,'r')
plt.show()
    