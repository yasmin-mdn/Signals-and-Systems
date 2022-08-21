import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
import math
def sinc(t,n,T):
    tmp=(np.sin(np.pi*(t-n*T)/T))/(np.pi*(t-n*T)/T)
    if  math.isnan(tmp):
        return 1
    return tmp

#reading file and make it float
f=open("data2.txt",'r')
x1=f.readlines()
#parsing nombers
x=[]
for st in x1:
    x.append(float(st))



#الف
x2=x[::2]


#ب
x3=[]
xct=[]
T=2
for n in x2:
    x3.append(n)
for i in range(1,len(x),2):
    x3.insert(i,0)

for t in range(0,101):
    xc=0
    for n in range(0,len(x3)):
        xc+=x3[n]*sinc(t,n,T)
    xct.append(xc)



#پ
y=scipy.signal.decimate(x,2)



#ت
x4=[]
xct2=[]
for n in y:
    x4.append(n)
for i in range(1,len(x),2):
    x4.insert(i,0)

for t in range(0,101):
    xc2=0
    for n in range(0,len(x4)):
        xc2+=x4[n]*sinc(t,n,T)
    xct2.append(xc2)




#ث
a1=[]
for i in range(0,100):
    a1.append(np.sqrt(np.mean((x[i]-xct[i])**2)))

a2=[]
for i in range(0,100):
    a2.append(np.sqrt(np.mean((x[i]-xct2[i])**2)))


b1=[]
for i in range(1,100,2):
    #b1.append(x[i]-xct[i])
    b1.append(np.sqrt(np.mean((x[i]-xct[i])**2)))

b2=[]
for i in range(1,100,2):
    #b2.append(x[i]-xct2[i])
    b2.append(np.sqrt(np.mean((x[i]-xct2[i])**2)))


c1=[]
for i in range(0,100,2):
    #c1.append(x[i]-xct[i])
    c1.append(np.sqrt(np.mean((x[i]-xct[i])**2)))

c2=[]
for i in range(0,100,2):
   # c2.append(x[i]-xct2[i])
    c2.append(np.sqrt(np.mean((x[i]-xct2[i])**2)))

print("///")
#بامقایسه نتایج از مورد ث در میابیم برای بازسازی سیگنال به طورکلی مناسب تر است ابتدا فیلتر را اعمال و 
# سپس نرخ نمونه برداری را کاهش دهیم چون سیگنال بازسازی شده با دقت بیشتری به سیگنال اصلی شبیه خواهد بود
#و با اینکار احتمال وقوع آلیاسینگ را کاهش داده ایم