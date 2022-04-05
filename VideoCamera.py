import datetime
from tkinter import *
import time
import tkinter.ttk as ttk
from tkinter.ttk import Style
timeis = time.strftime("%Y%m%d-%H%M%S")
filename = timeis + ".mp4"
import numpy as np
import cv2

window = Tk()
window.geometry("342x53")
ttk.Style().theme_use('clam')
HIlabel = Label(text="Hello ! Welcome to this video recorder.", font="Lucida", bg='black', fg='white', height=1, width=30)
HIlabel.grid(column=5500,row=1)

def recorderbutton():
    cap = cv2.VideoCapture(0)  
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))
    
    while(True):


        ret, frame = cap.read() 
        if ret:


            font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    


            dt = str(datetime.datetime.now())
    


            frame = cv2.putText(frame, dt,
                                (10, 100),
                                font, 1,
                                (210, 155, 155),
                                4, cv2.LINE_8)






        out.write(frame) 


        cv2.imshow('Original', frame)
    

    


        if cv2.waitKey(1) & 0xFF == ord('a'):
            break

    cv2.destroyAllWindows()

startrecbutton = Button(text = "Start recording",command=recorderbutton)
startrecbutton.grid(row=5, column=5500)
window.mainloop()