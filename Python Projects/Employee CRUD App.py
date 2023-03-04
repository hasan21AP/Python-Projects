from tkinter import *
from tkinter import messagebox
import sqlite3


def insert_data():
    id = enterid.get()
    name = entername.get()
    dept = enterdept.get()
    if id == "" or name == "" or dept == "":
        messagebox.showerror("Error Cannot Insert","All the fields are required!")
    else:
        myDB = sqlite3.connect("employee.db")
        myCR = myDB.cursor()
        myCR.execute("CREATE TABLE IF NOT EXISTS empdetails(empID integer PRIMARY KEY,empName text,empDept text)")
        myCR.execute(f"INSERT INTO empdetails(empID,empName,empDept) VALUES({id},'{name}','{dept}')")
        myDB.commit()

        show_data()

        messagebox.showinfo("Insert Status","Data inserted successfully")

        enterid.delete(0,"end")
        entername.delete(0,"end")
        enterdept.delete(0,"end")


        myDB.close()
        
def update_data():
    id = enterid.get()
    name = entername.get()
    dept = enterdept.get()
    if id == "" or name == "" or dept == "":
        messagebox.showerror("Error Cannot Udate","All the fields are required!")
    else:
        myDB = sqlite3.connect("employee.db")
        myCR = myDB.cursor()
        myCR.execute(f"UPDATE empdetails SET empName='{name}',empDept='{dept}' WHERE empID={id}")
        myDB.commit()

        show_data()

        messagebox.showinfo("Update Status","Data updated successfully")

        enterid.delete(0,"end")
        entername.delete(0,"end")
        enterdept.delete(0,"end")


        myDB.close()
        

def fetch_data():
    id = enterid.get()
    if id=="":
        messagebox.showerror("Error Cannot Fetch","All the fields are required!")
    else:
        myDB = sqlite3.connect("employee.db")
        myCR = myDB.cursor()
        myCR.execute(f"SELECT *FROM empdetails WHERE empID={id}")
        myDB.commit()
        rows = myCR.fetchall()
        for row in rows:
            entername.insert(0,row[1])
            enterdept.insert(0,row[2])

        myDB.close()

def delete_data():
    id = enterid.get()
    if id=="":
        messagebox.showerror("Error Cannot Fetch","All the fields are required!")
    else:
        myDB = sqlite3.connect("employee.db")
        myCR = myDB.cursor()
        myCR.execute(f"DELETE FROM empdetails WHERE empID={id}")
        myDB.commit()
            
        enterid.delete(0,"end")
        entername.delete(0,"end")
        enterdept.delete(0,"end")
        
        show_data()

        messagebox.showinfo("Delete Status","Data deleted successfully")

        myDB.close()

def reset_fields():
    enterid.delete(0,"end")
    entername.delete(0,"end")
    enterdept.delete(0,"end")



def show_data():
    myDB = sqlite3.connect("employee.db")
    myCR = myDB.cursor()
    myCR.execute("SELECT *FROM empdetails")
    myDB.commit()

    rows = myCR.fetchall()
    showdata.delete(0,showdata.size())

    for row in rows:
        addData = str(row[0])+" "+row[1]+"  "+row[2]
        showdata.insert(showdata.size()+1,addData)
        
    myDB.close()


window = Tk()

window.title("Employee CRUD App")

window_width = 600
window_height = 600

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2)-(window_width/2))
y = int((screen_height/2)-(window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width,window_height,x,y))

empid = Label(window,text="Employee ID",font=("Serif",12))
empid.place(x=20,y=30)

empname = Label(window,text="Employee Name",font=("Serif",12))
empname.place(x=20,y=60)

empdept = Label(window,text="Employee Dept",font=("Serif",12))
empdept.place(x=20,y=90)

enterid = Entry(window)
enterid.place(x=170,y=30)

entername = Entry(window)
entername.place(x=170,y=60)

enterdept = Entry(window)
enterdept.place(x=170,y=90)

insert_button = Button(window,text="Insert",font=("Sans",12),command=insert_data)
insert_button.place(x=20,y=160)

update_button = Button(window,text="Update",font=("Sans",12),command=update_data)
update_button.place(x=80,y=160)


fetch_button = Button(window,text="Fetch",font=("Sans",12),command=fetch_data)
fetch_button.place(x=150,y=160)

delete_button = Button(window,text="Delete",font=("Sans",12),command=delete_data)
delete_button.place(x=210,y=160)

reset_button = Button(window,text="Reset",font=("Sans",12),command=reset_fields)
reset_button.place(x=20,y=210)

showdata = Listbox(window,width=40,height=20)
showdata.place(x=330,y=30)


window.mainloop()
