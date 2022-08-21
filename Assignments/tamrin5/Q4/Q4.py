from scipy.io import wavfile as wav
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
rate, data = wav.read('speech.wav')
if type(data[0]) == list:
    data = data[:,0]

N = int(rate / 2)
a=[1]
a1=[0.5]
a2=[-0.5]
b=[1]
a1=np.concatenate([a,np.zeros(N-1),a1])
y=signal.lfilter(b,a1,data)
wav.write("res1.wav", rate, y.astype(data.dtype))

a2=np.concatenate([a,np.zeros(N-1),a2])
y=signal.lfilter(b,a2,data)
wav.write("res2.wav", rate, y.astype(data.dtype))
