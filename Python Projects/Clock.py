from tkinter import *
from time import strftime
import pygame

def time_clock():
    time_string = strftime("%I:%M:%S")
    time_label.config(text=time_string)

    day_string = strftime("%A  %d,%Y")
    day_label.config(text=day_string)
    window.after(1000,time_clock)
def play():
    pygame.mixer.music.load("Charlotte Ost 40-Haru No Hi.mp3")
    pygame.mixer.music.play()



window = Tk()
pygame.init()

window.title("Alarm Clock")

time_label = Label(window,text="",font=("Arial",20),bg="#000000",fg="#0000FF",width=20,height=3)
time_label.pack()

day_label = Label(window,text="",font=("Ink free",28))
day_label.pack()

play()

time_clock()

window.mainloop()