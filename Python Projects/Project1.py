from tkinter import *
def replace_word():
    global str

    word_replace = Enterword_replace.get()
    word_replacement = Enterword_replacement.get()
    newstr = str.replace(word_replacement,word_replace)
    label.config(text=newstr)



window = Tk()

str = "Hello everybody I'm Hasan, and today I'm ganna teach how to code in python."
label = Label(window,text=str,bg="black",fg="green",font=("Comic Sans MS",16))
label.pack()
button = Button(window,text="Replace word",command=replace_word)
button.pack()
label_replace = Label(window,text="Your word")
label_replace.pack()
Enterword_replace = Entry(window)
Enterword_replace.pack()
label_replacement = Label(window,text="The word")
label_replacement.pack()
Enterword_replacement = Entry(window)
Enterword_replacement.pack()
window.geometry("700x700")
window.mainloop()
