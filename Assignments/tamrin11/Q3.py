import numpy as np
import scipy
from wave import Wave_read,Wave_write
import wave
import math
from scipy.io import wavfile
import matplotlib.pyplot as plt

def LowpassFilter(delta,omegas,omegap):
    omegac=(omegas+omegap)/2
    M=0
    L=0
    wn=[]
    window_name=""
    deltaomega=omegas-omegap
    if delta>=0.09:
        window_name="Rectangular"
        L=int(1.8*np.pi/deltaomega)
    elif delta<0.09 and delta>=0.05:
        window_name="Bartlett"
        L=int(6.1*np.pi/deltaomega)
    elif delta>=0.0063 and delta<0.05:
        window_name="Hann"
        L=int(6.2*np.pi/deltaomega)
    elif delta>=0.0022 and delta<0.0063:
        window_name="Hamming"
        L=int(6.6*np.pi/deltaomega)
    elif delta<=0.0022:
        window_name="Blackman"
        L=int(11*np.pi/deltaomega)
    if L%2==0:
        M=L
    else:
        M=L-1
    n=np.arange(M+1)
    hlp=np.sinc(omegac/np.pi*(n-M/2))/np.pi*omegac
    if window_name=="Rectangular":
        for n in range(0,M+1):
            wn.append(1)
    elif window_name=="Bartlett":
        for n in range(0,M/2+1):
            wn.append(2*n/M)
        for n in range(n/M+1,M+1):
            wn.append(2-2*n/M)
    elif  window_name=="Hann":
            wn=(0.5-0.5*np.cos(2*np.pi*n/M))
    elif window_name=="Hamming":
            wn=(0.54 - 0.46 *np.cos(2*np.pi*n/M))
    elif window_name=="Blackman":
            wn=(0.42 - 0.5*np.cos(2*np.pi*n/M) + 0.08*np.cos(4*np.pi*n/M))
    h=hlp*wn
    return h

def  HighpassFilter(delta,omegas,omegap):
    omegac=(omegas+omegap)/2
    M=0
    L=0
    wn=[]
    window_name=""
    deltaomega=omegas-omegap
    if delta>=0.09:
        window_name="Rectangular"
        L=int(1.8*np.pi/deltaomega)
    elif delta<0.09 and delta>=0.05:
        window_name="Bartlett"
        L=int(6.1*np.pi/deltaomega)
    elif delta>=0.0063 and delta<0.05:
        window_name="Hann"
        L=int(6.2*np.pi/deltaomega)
    elif delta>=0.0022 and delta<0.0063:
        window_name="Hamming"
        L=int(6.6*np.pi/deltaomega)
    elif delta<=0.0022:
        window_name="Blackman"
        L=int(11*np.pi/deltaomega)
    if L%2==0:
        M=L
    else:
        M=L-1
    hhp=[]
    h=[]
    n=np.arange(M+1)
    for t in range(M+1):
        hhp.append(np.sinc((omegac-np.pi)/np.pi*(t-M/2))/np.pi*omegac*math.pow(-1,t))
    if window_name=="Rectangular":
        for n in range(0,M+1):
            wn.append(1)
    elif window_name=="Bartlett":
        for n in range(0,M/2+1):
            wn.append(2*n/M)
        for n in range(n/M+1,M+1):
            wn.append(2-2*n/M)
    elif  window_name=="Hann":
            wn=(0.5-0.5*np.cos(2*np.pi*n/M))
    elif window_name=="Hamming":
            wn=(0.54 - 0.46 *np.cos(2*np.pi*n/M))
    elif window_name=="Blackman":
            wn=(0.42 - 0.5*np.cos(2*np.pi*n/M) + 0.08*np.cos(4*np.pi*n/M))
    for i in range(0,M+1):
        h.append(hhp[i]*wn[i])
    return h


def Filter(filtertype,delta,omegas,omegap):
    if filtertype=="Lowpass":
        return LowpassFilter(delta,omegas,omegap)
    if filtertype=="Highpass":
       return HighpassFilter(delta,omegas,omegap)

#//////////////////////////////////////////////

fs, data = wavfile.read('voice.wav')
if type(data[0]) == list:
    data = data[:,0]
#owl
h=Filter("Lowpass",0.003,2*np.pi/50,np.pi/50)
f=np.convolve(data,h)
wavfile.write("owlsound.wav",fs,f.astype(data.dtype))
#ring
h=Filter("Highpass",0.003,2*np.pi/50,np.pi/50)
f=np.convolve(data,h)
wavfile.write("ringsound.wav",fs,f.astype(data.dtype))
