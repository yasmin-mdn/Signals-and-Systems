from scipy.io import wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
import os
import scipy.signal


def DTMF1(signal, rate):

  result=''
  ##################################

  N=len(signal)
  f_signal=np.fft.fft(signal)
  frq_arr=[]
  for k in range(0,len(f_signal)):
      frq_arr.append((k*rate)/N)
  mag_f=np.abs(f_signal)


  tmp=[]
  idx=[]
  for m in range(0,8):
      tmp.append(np.abs(mag_f[m]))
      idx.append(m)
  for k in range(0,int(len(mag_f)/2)):
      for l in range(7,-1,-1):
          if(np.abs(mag_f[k]))>np.abs(tmp[l]):
              t=tmp[0]
              i=idx[0]
              tmp.remove(t)
              idx.remove(i)
              tmp.append(np.abs(mag_f[k]))
              idx.append(k)
              tmp.sort()
              idx.sort()
              break          

  res=[]
  for i in idx:
      res.append(frq_arr[i])
  
  for i in range(0,8):
      for j in range(i+1,8):
        if res[i]>697-10 and res[i]<697+10:
          if res[j]>1209-10 and res[j]<1209+10:
              result='1'
              break
          elif res[j]>1336-10 and  res[j]<1336+10:
              result='2'
              break
          elif  res[j]>1477-10 and  res[j]<1477+10:
              result='3'
              break
          elif  res[j]>1633-10 and  res[j]<1633+10:
              result='A'
              break
        elif res[i]>770-10 and res[i]<770+10:
          if  res[j]>1209-10 and  res[j]<1209+10:
              result='4'
              break
          elif  res[j]>1336-10 and  res[j]<1336+10:
              result='5'
              break
          elif  res[j]>1477-10 and  res[j]<1477+10:
              result='6'
              break
          elif  res[j]>1633-10 and  res[j]<1633+10:
              result='B'
              break
        elif res[i]>852-10 and res[i]<852+10:
          if  res[j]>1209-10 and  res[j]<1209+10:
              result='7'
              break
          elif  res[j]>1336-10 and  res[j]<1336+10:
              result='8'
              break
          elif  res[j]>1477-10 and  res[j]<1477+10:
              result='9'
              break
          elif  res[j]>1633-10 and  res[j]<1633+10:
              result='C'
              break
        elif res[i]>941-10 and res[i]<941+10:
          if  res[j]>1209-10 and  res[j]<1209+10:
              result='*'
              break
          elif  res[j]>1336-10 and  res[j]<1336+10:
              result='0'
              break
          elif  res[j]>1477-10 and  res[j]<1477+10:
              result='#'
              break
          elif  res[j]>1633-10 and  res[j]<1633+10:
              result='D'
              break


  return result




def DTMF(signal, rate):
    result =''
    st=''
    for i in range(0,len(signal)-int(rate/5),int(rate/20)):
      x=[]
      
      if(signal[i] != 0):
        for j in range(0,int(rate/5)):
          x.append(signal[i+j])
        st=st+DTMF1(x,rate)
        #result=result+DTMF1(x,rate)


#####3.6666
  #  for key in st:
  #      if not(key in result):
  #          result=result+key


  #####1.6
    if len(st)>0:
        result=result+st[0]
        for key in st[1:]:
           if (key != result[len(result)-1]):
               result=result+key

   


    return result

#[rate,signal]=wav.read("1.wav")
#print(DTMF(signal,rate))