from scipy.io import wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
import os
import scipy


			
			

def DTMF(signal, rate):
    result=''
    ##################################

    N=len(signal)
    f_signal=np.fft.fft(signal)
    frq_arr=[]
    for k in range(0,len(f_signal)):
        frq_arr.append((k*rate)/N)
    mag_f=np.abs(f_signal)
    Max=Max2=mag_f[0]
    idx=0
    idx2=0
    for k in range(0,int(len(mag_f)/2)):
        if mag_f[k]>Max:
            Max2=Max
            idx2=idx
            Max=mag_f[k]
            idx=k
        elif mag_f[k]>Max2 and mag_f[k]<Max:
            Max2=mag_f[k]
            idx2=k
    
            
    res=frq_arr[idx]       
    res2=frq_arr[idx2]
    if res>res2:
        tmp=res2
        res2=res
        res=tmp

    if res>697-3 and res<697+3:
        if res2>1209-3 and res2<1209+3:
            result='1'
        elif res2>1336-3 and res2<1336+3:
            result='2'
        elif res2>1477-3 and res2<1477+3:
            result='3'
        elif res2>1633-5 and res2<1633+5:
            result='A'

    elif res>770-3 and res<770+3:
        if res2>1209-3 and res2<1209+3:
            result='4'
        elif res2>1336-3 and res2<1336+3:
            result='5'
        elif res2>1477-3 and res2<1477+3:
            result='6'
        elif res2>1633-5 and res2<1633+5:
            result='B'
    elif res>852-3 and res<852+3:
        if res2>1209-3 and res2<1209+3:
            result='7'
        elif res2>1336-3 and res2<1336+3:
            result='8'
        elif res2>1477-3 and res2<1477+3:
            result='9'
        elif res2>1633-5 and res2<1633+5:
            result='C'
    elif res>941-3 and res<941+3:
        if res2>1209-3 and res2<1209+3:
            result='*'
        elif res2>1336-3 and res2<1336+3:
            result='0'
        elif res2>1477-3 and res2<1477+3:
            result='#'
        elif res2>1633-5 and res2<1633+5:
            result='D'


    return result

[rate,signal]=wav.read('2.wav')
print(DTMF(signal,rate))