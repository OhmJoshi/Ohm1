from tkinter import *
import tkinter as tk
import datetime
import qrcode
import image

window=Tk()
window.geometry("1000x500")
window.title("QRcode generator")

def generate():
    qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5)
    data = textval.get()
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    file_name=f'{time_stamp}.png'
    qr.add_data(data)
    qr.make(fit = True)
    img = qr.make_image(fill="black", back_color="white")
    img.save(file_name)
textval = StringVar()
link=Entry(window,textvariable=textval, width=75)
link.grid(row=0, column=0)
generatebutton=Button(text="Generate a QR code !", width=35, command=generate)
generatebutton.grid(row=2, column=0)
usage=Label(window,text="After entering a link to a site, click the 'Generate a QR code' button and check the folder in which this program is saved.")
usage.grid(row=3, column=0)

window.mainloop()
