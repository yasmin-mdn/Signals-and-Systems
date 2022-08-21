import scipy as sc
import math
import numpy as np
import matplotlib.pyplot as plt
N=11
x=[0,1,2,3,4,5,4,3,2,1,0]
y=[0,0,0,0,0,0,0,0,0,0,0]
j=np.complex(0,1)
def c(x):
    c=(1/len(x))*np.fft.fft(x)
    return c
print(c(x))

   


