import pyaudio
import numpy as np
import scipy as sc
import scipy.special
from tkinter import *
import os.path as path
#UI
#####################################
#rendering window
chaneltext=""
window=Tk()
window.title('Digital Radio')
window.resizable(0,0)
image1 = PhotoImage(file="radio1.gif")
w = image1.width()
h = image1.height()
window.geometry("%dx%d+0+0" % (w, h))
panel1 = Label(window, image=image1)
panel1.pack(side='top', fill='both', expand='yes')
panel1.image = image1

#display box
display=Text(window, bg='black',fg='green', font=("DIGITAL-7", 23),height=3.4,width=12,state=DISABLED)
display.place(x=239, y=207)
filePath = ""
freq = 0

#filename component
E1 = Entry(window, bd =5 , width = 26)
E1.place(x=240, y=177)
#freq input component
E2 = Entry(window, bd =5 , width = 21)
E2.place(x=240, y=377)

#stream
p = pyaudio.PyAudio()
player = p.open(format=pyaudio.paInt16, channels=1, rate=240000, output=True)
player.stop_stream()
player.close()
p.terminate()

#channel buttons functions
def AvaButtonClicked():    
    filePath = fileButton()
    if( filePath != ""):
        chaneltext= "Ava"
        display.config(state=NORMAL, fg = "green")
        display.delete('1.0', END)
        display.insert(INSERT,"\n      " + chaneltext)
        display.config(state=DISABLED)
        window.update_idletasks()
        window.update()        
        StartRadio( filePath  , 96000)        

def FarhangButtonClicked():
    filePath =fileButton()
    if(filePath != ""):
        chaneltext="Farhang"
        display.config(state=NORMAL, fg = "green")
        display.delete('1.0', END)
        display.insert(INSERT,"\n    " +chaneltext)
        display.config(state=DISABLED)
        window.update_idletasks()
        window.update()        
        StartRadio( filePath  , 240000)        

def EghtesadButtonClicked():
    filePath = fileButton()
    if(filePath != ""):
        chaneltext="Eghtesad"
        display.config(state=NORMAL, fg = "green")
        display.delete('1.0', END)
        display.insert(INSERT,"\n   " +chaneltext)
        display.config(state=DISABLED)
        window.update_idletasks()
        window.update()        
        StartRadio( filePath  , 144000)

def GoftogooButtonClicked():    
    filePath = fileButton()
    if(filePath != ""):
        chaneltext="Goftogoo"
        display.config(state=NORMAL, fg = "green")
        display.delete('1.0', END)
        display.insert(INSERT,"\n   " +chaneltext)
        display.config(state=DISABLED)
        window.update() 
        window.update_idletasks()       
        StartRadio( filePath  , 288000)            

#file validation returns filepath
def fileButton():
    player.stop_stream()
    player.close()
    p.terminate()
    filePath = E1.get()
    if(filePath == "" ):
        #error
        display.fg = "red"
        display.config(state=NORMAL, fg = "red")
        display.delete('1.0', END)
        display.insert(INSERT,"\n   enter file " )
        display.config(state=DISABLED)
        return ""

    elif(filePath.endswith(".txt") == False):        
        display.config(state=NORMAL , fg = "red")
        display.delete('1.0', END)
        display.insert(INSERT,"\nwrong format" )
        display.config(state=DISABLED)
        return ""

    elif  (path.exists(filePath) == False ):
        display.fg = "red"
        display.config(state=NORMAL, fg = "red")
        display.delete('1.0', END)
        display.insert(INSERT,"\n no such file" )
        display.config(state=DISABLED)
        return ""

    else :                
        return filePath

#freq type validation  & start radio
def PlayButton():    
    freq = E2.get()
    #errors
    if(freq == ""):
        display.fg = "red"
        display.config(state=NORMAL, fg = "red")
        display.delete('1.0', END)
        display.insert(INSERT,"\n enter \n frequency" )
        display.config(state=DISABLED)
    if( freq.isnumeric()== False):
        display.fg = "red"
        display.config(state=NORMAL, fg = "red")
        display.delete('1.0', END)
        display.insert(INSERT,"\n enter \n number" )
        display.config(state=DISABLED)
    else :
        path = fileButton()
        dis = " " + str(freq) + " KHz"
        if(path != ""):            
            if(int(freq) == 96):
                dis = dis + ":\n Ava"
            elif(int(freq) == 144):
                dis = dis + ":\n Eghtesad"
            elif(int(freq) == 288):
                dis = dis + ":\n Goftogoo"
            elif(int(freq) == 240):
                dis = dis + ":\n Farhang"

            display.config(state=NORMAL, fg = "green")
            display.delete('1.0', END)
            display.insert(INSERT, dis)
            display.config(state=DISABLED)

            StartRadio( path , int(freq)*1000)   

         
#placing channel buttons
#ava
btn_Ava=Button(window, text="آوا", bg='#d9d9d9' , command = AvaButtonClicked)
btn_Ava.place(x=160, y=185)

#Farhang
btn_farhang=Button(window, text="فرهنگ", bg='#d9d9d9' , command = FarhangButtonClicked)
btn_farhang.place(x=460, y=185)

#eghtesad
btn_Eghtesad=Button(window, text="اقتصاد", bg='#d9d9d9' , command =EghtesadButtonClicked)
btn_Eghtesad.place(x=510, y=185)


#Goftogoo
btn_Goftogoo=Button(window, text="گفت و گو", bg='#d9d9d9' , command = GoftogooButtonClicked)
btn_Goftogoo.place(x=90, y=185)

#Play
btn_Ava=Button(window, text="پخش", bg='#d9d9d9' , command = PlayButton)
btn_Ava.place(x=380, y=377)


#main functions of radio
CHUNK = 48000
def extractor( freq ):

    def kaiser(Dw , S ):    
        A = -20*np.log10(S) 

        B = 0.5842*((A-21)**0.4) + 0.07886*(A-21)        

        M = (A-8)/(2.285*Dw) 

        M = np.ceil(M)

        if M%2==1:
            M = M+1
        
        M = int(M)

        a = M/2 #delay

        n = np.arange(M+1)
        w = (scipy.special.i0(B*np.sqrt(1-((n-a)/a)**2)))/(scipy.special.i0(B))

        return (w , M)

    omega = freq * np.pi *2 / 480000

    #Filters func#################################################    
    wc = np.pi /30    
    w , M = kaiser( np.pi/300 , 0.003)    

    n = np.arange(0,M+1)

    hd = np.sinc(wc / np.pi *(n- M/2) ) / np.pi * wc
    h = hd * w    
    ##############################################################

    n = np.arange(0 , CHUNK)
    shift = np.cos( omega *n)
    
    return (shift , h , M , omega)    

def StartRadio(filePath , freq):

    p = pyaudio.PyAudio()
    player = p.open(format=pyaudio.paInt16, channels=1, rate=240000, output=True, frames_per_buffer=CHUNK)
                
    File = open(filePath)

    shift , h , M , omega = extractor(freq)
    M = int(M)
    buffer = np.zeros(M)
    while True:
        window.update()
        window.update_idletasks()

        data = []
        for i in range(CHUNK):
            line = File.readline()
            if line=='':
                break
            data.append(int(line))

        if(len(data) == 0):
            break 

        if(len(data) < CHUNK):        
            n = np.arange(0 , len(data))
            shift = np.cos( omega * n)

        data = data * shift
        x = np.concatenate([buffer , data])

        y = np.convolve( x , h , 'valid')
        y = y[::2]
        y = 5*y
        player.write(y.astype(np.int16), len(y))
        
        buffer = x[-M:]

    player.stop_stream()
    player.close()
    p.terminate()
    File.close()

window.mainloop()