from random import seed
import mysql.connector
from tkinter import *
from tkinter import messagebox


def manager_window():
    window = Toplevel()
    window.title("إضافة صنف")
    
    width = 600
    height = 600

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width/2)-(width/2))
    y = int((screen_height/2)-(height/2))

    window.geometry(f"{width}x{height}+{x}+{y}")



    label_barcod = Label(window,text="الباركود",font=("Arial",20))
    label_barcod.place(x=450,y=15)

    enter_barcod = Entry(window,bd=2,border=5)
    enter_barcod.place(x=425,y=50)



    label_item = Label(window,text="الصنف",font=("Arial",20))
    label_item.place(x=315,y=15)

    enter_item = Entry(window,bd=2,border=5)
    enter_item.place(x=280,y=50)



    label_price = Label(window,text="السعر",font=("Arial",20))
    label_price.place(x=200,y=15)

    enter_price = Entry(window,bd=2,border=5,width=12)
    enter_price.place(x=190,y=50)



    label_quintity = Label(window,text="العدد",font=("Arial",20))
    label_quintity.place(x=130,y=15)

    enter_quintity = Entry(window,bd=2,border=5,width=6)
    enter_quintity.place(x=130,y=50)



    label_sum = Label(window,text="الإجمالي",font=("Arial",20))
    label_sum.place(x=40,y=15)
    
    enter_sum = Entry(window,bd=2,border=5,width=12)
    enter_sum.place(x=40,y=50)


    

    def accept_products():
        product_barcod = enter_barcod.get()
        product_name = enter_item.get()
        product_quintity = enter_quintity.get()
        product_price = enter_price.get()
        
        if product_barcod == "" or product_name == "" or product_quintity == "" or product_price == "":
            messagebox.showwarning("Fields empty","All the fields are required")
        else:
            db = mysql.connector.connect(host="localhost",user="root",passwd="aabbccN77",auth_plugin="mysql_native_password",database="products")
            curdb = db.cursor()
            curdb.execute("CREATE TABLE IF NOT EXISTS addproducts(barcod int(13) PRIMARY KEY,name_item VARCHAR(255),price float,quintity int)")
            curdb.execute(f"INSERT INTO addproducts VALUES({product_barcod},'{product_name}',{product_price},{product_quintity})")
            db.commit()
            messagebox.showinfo("Insert Status","Product Inserted Successfully")
            enter_barcod.delete(0,"end")
            enter_item.delete(0,"end")
            enter_quintity.delete(0,"end")
            enter_price.delete(0,"end")
            enter_sum.delete(0,"end")
            db.close()
    
    def sum_items():
        product_quintity = enter_quintity.get()
        product_price = enter_price.get()

        product_sum = float(product_price) * float(product_quintity)
        enter_sum.insert(0,product_sum)
        


    add_button = Button(window,text="إضافة",font=("Arial",16),command=accept_products)
    add_button.place(x=200,y=100)
    

    sum_button = Button(window,text="الإجمالي",font=("Arial",16),command=sum_items)
    sum_button.place(x=300,y=100)

    # list_menu = Listbox(window,height=50,width=99,font=("Consolas",12))
    # list_menu.place(x=1,y=190)

    

def employee_window():
    window = Toplevel()
    window.title("المبيعات")
    width = 600
    height = 600

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width/2)-(width/2))
    y = int((screen_height/2)-(height/2))

    window.geometry(f"{width}x{height}+{x}+{y}")

    label_barcod = Label(window,text="الباركود",font=("Arial",20))
    label_barcod.place(x=450,y=15)

    enter_barcod = Entry(window,bd=2,border=5)
    enter_barcod.place(x=425,y=50)



    label_item = Label(window,text="الصنف",font=("Arial",20))
    label_item.place(x=315,y=15)

    enter_item = Entry(window,bd=2,border=5)
    enter_item.place(x=280,y=50)



    label_price = Label(window,text="السعر",font=("Arial",20))
    label_price.place(x=200,y=15)

    enter_price = Entry(window,bd=2,border=5,width=12)
    enter_price.place(x=190,y=50)



    label_quintity = Label(window,text="العدد",font=("Arial",20))
    label_quintity.place(x=130,y=15)

    enter_quintity = Entry(window,bd=2,border=5,width=6)
    enter_quintity.place(x=130,y=50)



    label_sum = Label(window,text="الإجمالي",font=("Arial",20))
    label_sum.place(x=40,y=15)
    
    enter_sum = Entry(window,bd=2,border=5,width=12)
    enter_sum.place(x=40,y=50)

    def sell_products():
        product_barcod = enter_barcod.get()
        product_name = enter_item.get()
        product_quintity = enter_quintity.get()
        product_price = enter_price.get()
        
        if product_barcod == "" or product_name == "" or product_quintity == "" or product_price == "":
            messagebox.showwarning("Fields empty","All the fields are required")
        else:
            db = mysql.connector.connect(host="localhost",user="root",passwd="aabbccN77",auth_plugin="mysql_native_password",database="products")
            curdb = db.cursor()
            curdb.execute("CREATE TABLE IF NOT EXISTS sellproducts(barcod int(13) PRIMARY KEY,name_item VARCHAR(255),price float,quintity int)")
            curdb.execute(f"INSERT INTO sellproducts SELECT *FROM addproducts WHERE barcod={product_barcod},name_item='{product_name}',price={product_price},quintity={product_quintity} )")
            db.commit()
            messagebox.showinfo("Insert Status","Product Inserted Successfully")
            enter_barcod.delete(0,"end")
            enter_item.delete(0,"end")
            enter_quintity.delete(0,"end")
            enter_price.delete(0,"end")
            enter_sum.delete(0,"end")
            db.close()
    
    def sum_items():
        product_quintity = enter_quintity.get()
        product_price = enter_price.get()

        product_sum = float(product_price) * float(product_quintity)
        enter_sum.insert(0,product_sum)
        


    add_button = Button(window,text="بيع",font=("Arial",16),width=5,command=sell_products)
    add_button.place(x=200,y=100)
    

    sum_button = Button(window,text="الإجمالي",font=("Arial",16),command=sum_items)
    sum_button.place(x=300,y=100)


window = Tk()
window.title("SuperMarket Cashier")

label = Label(text="اكسراي قرطاسية",font=("Consolas",40),bg="white")
label.pack()

add_items = Button(text="صنف إضافة",font=("Consolas",20),bg="black",width=9,fg="blue",command=manager_window)
add_items.pack()

selas_button = Button(text="المبيعات",font=("Consolas",20),bg="black",width=9,fg="blue",command=employee_window)
selas_button.pack()


width = 600
height = 600

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2)-(width/2))
y = int((screen_height/2)-(height/2))

window.geometry(f"{width}x{height}+{x}+{y}")

window.mainloop()