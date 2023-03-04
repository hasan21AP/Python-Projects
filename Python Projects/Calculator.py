from tkinter import *
from functools import reduce
def press_button(num):
    global equation_text
    equation_text += str(num)
    equation_label.set(equation_text)

def equal():
    global equation_text
    try:
        if "!" not in equation_text:
            total = str(eval(equation_text))
            equation_label.set(total)
            equation_text = total
        else:
            num = int(equation_text[:-1])
            listf = []
            for i in range(num):
                x = i + 1
                listf.append(x)
        f = reduce(lambda a,b:a*b,listf)
        foct = str(f)
        equation_label.set(foct)
        equation_text = foct
    except ZeroDivisionError:
        equation_label.set("You can't divide on zero!")
        equation_text = ""
    except SyntaxError:
        equation_label.set("SyntaxError")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

def foctroial():
    global equation_text
    equation_text += "!"
    equation_label.set(equation_text)

window = Tk()
window.title("Calculator")

icon = PhotoImage(file="calculator.png")
window.geometry("500x500")
window.iconphoto(True,icon)

equation_text = ""
equation_label = StringVar()

label = Label(window,textvariable=equation_label,font=("Consolas",20),width=24,height=2,bg="white")
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame,text=1,font=35,width=9,height=4,bg="black",fg="white",command=lambda:press_button(1))
button1.grid(row=0,column=0)

button2 = Button(frame,text=2,font=35,width=9,height=4,bg="black",fg="white",command=lambda:press_button(2))
button2.grid(row=0,column=1)

button3 = Button(frame,text=3,font=35,width=9,height=4,bg="black",fg="white",command=lambda:press_button(3))
button3.grid(row=0,column=2)

button4 = Button(frame,text=4,font=35,width=9,height=4,bg="black",fg="white",command=lambda:press_button(4))
button4.grid(row=1,column=0)

button5 = Button(frame,text=5,font=35,width=9,height=4,bg="black",fg="white",command=lambda:press_button(5))
button5.grid(row=1,column=1)

button6 = Button(frame,text=6,font=35,width=9,height=4,bg="black",fg="white",command=lambda:press_button(6))
button6.grid(row=1,column=2)

button7 = Button(frame,text=7,font=35,width=9,height=4,bg="black",fg="white",command=lambda:press_button(7))
button7.grid(row=2,column=0)

button8 = Button(frame,text=8,font=35,width=9,height=4,bg="black",fg="white",command=lambda:press_button(8))
button8.grid(row=2,column=1)

button9 = Button(frame,text=9,font=35,width=9,height=4,bg="black",fg="white",command=lambda:press_button(9))
button9.grid(row=2,column=2)

button0 = Button(frame,text=0,font=35,width=9,height=4,bg="black",fg="white",command=lambda:press_button(0))
button0.grid(row=3,column=1)

plus = Button(frame,text="+",font=35,width=9,height=4,bg="black",fg="white",command=lambda:press_button("+"))
plus.grid(row=0,column=3)

munis = Button(frame,text="-",font=35,width=9,height=4,bg="black",fg="white",command=lambda:press_button("-"))
munis.grid(row=1,column=3)

multiply = Button(frame,text="×",font=35,width=9,height=4,bg="black",fg="white",command=lambda:press_button("*"))
multiply.grid(row=2,column=3)

division = Button(frame,text="÷",font=35,width=9,height=4,bg="black",fg="white",command=lambda:press_button("/"))
division.grid(row=3,column=3)

equation = Button(frame,text="=",font=35,width=9,height=4,bg="black",fg="white",command=lambda:equal())
equation.grid(row=3,column=2)

clear_label = Button(frame,text="clear",font=35,width=9,height=4,bg="orange",fg="black",command=lambda:clear())
clear_label.grid(row=3,column=0)

foctroial_label = Button(frame,text="!",font=35,width=9,height=4,bg="black",fg="white",command=lambda:foctroial())
foctroial_label.grid(row=4,column=2)

window.mainloop()