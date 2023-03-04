import mysql.connector
from tkinter import *
from tkinter.messagebox import *


window = Tk()
window.title("Library Managment App")

label = Label(window,text="Welcome to our labrary",font=("Consolas",25),fg="black")
label.pack()


class Library:

    def __init__(self,name,booksList):
        
        self.name = mysql.connector.connect(host="localhost",user="root",passwd="aabbccN77",auth_plugin="mysql_native_password",database=f"'{name}'")
        mycur = self.name.cursor()
        mycur.execute(f"CREATE TABLE IF NOT EXISTS {booksList} (bookId int PRIMARY KEY,bookName varchar(255))")
        self.name.commit()
        self.name.close()

    def addBook(self,booksList):

        bookId = int(input("Enter the ID of the book: "))
        bookName = input("Enter the Name of the book: ")

        db = mysql.connector.connect(host="localhost",user="root",passwd="aabbccN77",auth_plugin="mysql_native_password",database="books")
        mycur = db.cursor()
        mycur.execute(f"INSERT INTO {booksList} VALUES({bookId},'{bookName}') ")
        mycur.execute("SELECT *FROM bookslist")
        books = mycur.fetchall()
        for book in books:
            if bookName in book:
                print("Book already exists")
            else:
                mycur.execute(f"INSERT INTO bookslist VALUES({self.bookId},'{self.bookName}')")
                print("Book added")
        db.commit()
        db.close()
 
    def displayBooks(self):
        db = mysql.connector.connect(host="localhost",user="root",passwd="aabbccN77",auth_plugin="mysql_native_password",database="books")
        mycur = db.cursor()
        mycur.execute("SELECT *FROM bookslist")
        books = mycur.fetchall()
        for book in books:
            print(book)
        db.commit()
        db.close()

    def lendBook(self,booksList):
        userName = input("Enter the Name of the book: ")
        bookId = int(input("Enter the ID of the book: "))
        db = mysql.connector.connect(host="localhost",user="root",passwd="aabbccN77",auth_plugin="mysql_native_password",database="books")
        mycur = db.cursor()
        mycur.execute(f"CREATE TABLE IF NOT EXISTS bookslend(username VARCHAR(255)),FOREIGN KEY bookId REFERENCES '{booksList}'({bookId})")
        mycur.execute(f"INSERT INTO bookslend VALUES('{userName}')")
        print("Lended successfully")
        db.commit()
        db.close()
    def returnBook():
        bookName = input("Enter the Name of the book: ")
        userName = input("Enter the Name of the book: ")
        db = mysql.connector.connect(host="localhost",user="root",passwd="aabbccN77",auth_plugin="mysql_native_password",database="books")
        mycur = db.cursor()
        mycur.execute(f"DELETE FROM bookslend WHERE WHERE booksname = '{bookName}', username = '{userName}'")
        print("Lended successfully")
        db.commit()
        db.close()


def displaybooks():
    pass

def addbooks():
    pass

def lendbooks():
    pass

def returnbooks():
    pass


showbooks_button = Button(window,text="Display Books",font=("arial",20),bg="black",fg="white",command=displaybooks)
showbooks_button.pack()

addbooks_button = Button(window,text="  Add Books   ",font=("arial",20),bg="black",fg="white",command=addbooks)
addbooks_button.pack()

lendbooks_button = Button(window,text="  Lend Books ",font=("arial",20),bg="black",fg="white",command=lendbooks)
lendbooks_button.pack()

returnbooks_button = Button(window,text="Return Books ",font=("arial",20),bg="black",fg="white",command=returnbooks)
returnbooks_button.pack()


width = 500
height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (width/2))
y = int((screen_height/2) - (height/2))

window.geometry("{}x{}+{}+{}".format(width,height,x,y))

window.mainloop()