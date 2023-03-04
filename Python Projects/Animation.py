import time
from tkinter import *

xvelocity = 2
yvelocity = 2

WIDTH = 500
HEIGHT = 500

window = Tk()
window.title("Animation")
law = PhotoImage(file="Law.png")
background_photo = PhotoImage(file="Sea.png")

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

law_moving = canvas.create_image(0,0,image=law,anchor=NW)
background = canvas.create_image(0,0,image=background_photo,anchor=NW)

image_width = law.width()
image_height = law.height()

while True:
        coordinates = canvas.coords(law_moving)
        if (coordinates[0] >= WIDTH-image_width or coordinates[0] < 0):
            xvelocity = -xvelocity
        if (coordinates[1] >= HEIGHT-image_height or coordinates[1] < 0):
            yvelocity = -yvelocity
        canvas.move(law_moving,xvelocity,yvelocity)
        window.update()
        time.sleep(0.01)




window.mainloop()