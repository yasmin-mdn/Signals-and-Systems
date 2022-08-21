import soundfile as sf
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

def make_h(M):
    h=(1/M)*np.ones(M)
    return h


data, samplerate = sf.read('signal.wav')
if type(data[0]) == list:
    data = data[:,0]
data+=np.random.randn(data.shape[0])*0.025
#sf.write("res.wav", data.astype(data.dtype),samplerate)


h=make_h(20)
y=10*np.convolve(data,h,'full')
sf.write("M20.wav", y.astype(data.dtype),samplerate)

h=make_h(100)
y=20*np.convolve(data,h,'full')
sf.write("M100.wav", y.astype(data.dtype),samplerate)

h=make_h(2000)
y=300*np.convolve(data,h,'full')
sf.write("M2000.wav", y.astype(data.dtype),samplerate)