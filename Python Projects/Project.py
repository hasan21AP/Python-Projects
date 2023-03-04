from tkinter import *
import time 
from algorithms import window_resize

window = Tk()
window.title("Clock")



time_clock = StringVar()

label = Label(window,text=time_clock,font=("consals",40),bg="#000000",fg="#117C47",width=7,height=2)
label.pack()



window_resize(window,500,500)
window.mainloop()