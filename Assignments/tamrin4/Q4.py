import numpy as np 
import matplotlib.pyplot as plt 
from scipy import signal
from scipy.io.wavfile import read,write
import wave
[samplerate,x]=read("test.wav")
N=(int)(samplerate/2)
h1=signal.unit_impulse(3*N+1,0,float)
h2=(1/2)*signal.unit_impulse(3*N+1,N,float)
h3=(1/4)*signal.unit_impulse(3*N+1,2*N,float)
h4=(1/8)*signal.unit_impulse(3*N+1,3*N,float)
h=h1+h2+h3+h4
y=np.convolve(x,h,'full')

#plt.plot(y,'g')
#plt.plot(x,'r')
#plt.show()

#out_f = 'out3.wav'
write("res.wav", samplerate, y.astype(x.dtype))




