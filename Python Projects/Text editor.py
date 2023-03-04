from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os
from tkinter import filedialog,colorchooser,font

def newfile():
    text_area.delete(0.0,END)
    window.title("Untitled")

def savefile():
    file = filedialog.asksaveasfilename(initialfile="Untitled",defaultextension=".txt",filetypes=(("All files","*.*"),("Text file","*.txt")))
    if file is None:
        return
    else:
        try:
            window.title(os.path.basename(file))
            file =open(file,"w")
            file.write(text_area.get(1.0,END))
        except Exception:
            showerror(title="Error",text="Couldn't save the file")
        finally:
            file.close()



def openfile():
    file = filedialog.askopenfilename(defaultextension=".txt",filetypes=(("All files","*.*"),("Text file","*.txt")))
    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0,END)
        file = open(file,"r")
        text_area.insert(1.0,file.read())
    except Exception:
        showerror(title="Error",text="Couldn't open the file")
    finally:
        file.close()

def quit():
    text_area.destroy()

def copy():
    text_area.event_generate("<<Copy>>")

def cut():
    text_area.event_generate("<<Cut>>")

def paste():
    text_area.event_generate("<<Paste>>")

def about():
    showinfo("CopyRights","This my program ok!")

def change_color():
    color = colorchooser.askcolor()
    text_area.config(fg=color[1])
   

def change_font(*args):
    text_area.config(font=(font_name.get(),size_box.get()))

window = Tk()
#icon = PhotoImage(file="text editor.png")

window.title("Text editor")
#window.iconphoto(True,icon)


window_width = 500
window_height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2)-(window_width/2))
y = int((screen_height/2)-(window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width,window_height,x,y))

font_name = StringVar(window)
font_size = StringVar(window)

font_name.set("Arial")
font_size.set("25")

text_area = Text(window,font=(font_name.get(),font_size.get()))

scrollbar = Scrollbar(text_area)
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)
text_area.grid(sticky=N+S+W+E)
scrollbar.pack(side=RIGHT,fill=Y)
text_area.config(yscrollcommand=scrollbar.set)


frame = Frame(window)
frame.grid()

color_button = Button(frame,text="Color",command=change_color)
color_button.grid(row=0,column=0)

font_box = OptionMenu(frame,font_name,*font.families(),command=change_font)
font_box.grid(row=0,column=1)

size_box = Spinbox(frame,textvariable=font_size,from_=1,to=500,command=change_font)
size_box.grid(row=0,column=2)


menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar,tearoff=0)
edit_menu = Menu(menu_bar,tearoff=0)
help_menu = Menu(menu_bar,tearoff=0)

menu_bar.add_cascade(menu=file_menu,label="File")
menu_bar.add_cascade(menu=edit_menu,label="Edit")
menu_bar.add_cascade(menu=help_menu,label="Help")

file_menu.add_command(label="New",command=newfile)
file_menu.add_command(label="Open",command=openfile)
file_menu.add_command(label="Save",command=savefile)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=quit)

edit_menu.add_command(label="Copy",command=copy)
edit_menu.add_command(label="Cut",command=cut)
edit_menu.add_command(label="Paste",command=paste)

help_menu.add_command(label="About",command=about)



window.mainloop()
