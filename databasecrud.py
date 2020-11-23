from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
root=Tk()
root.title("radio")
root.geometry("800x500+0+0")

def add():
    if(text_field1.get('1.0',END)==" " or text_field2.get('1.0',END)==" " or text_field3.get('1.0',END)==" "):
        Messagebox.showinfo("INSERT STATUS","All fields are required")
    else:
        name=text_field1.get('1.0',END)
        contact=int(text_field2.get('1.0',END))
        age=int(text_field3.get('1.0',END))
        con=mysql.connect(host="localhost",user="root",password="root",database="python_tkinter")
        cursor=con.cursor()
        cursor.execute("insert into form values('%s',%d,%d)"%(name,contact,age))
        cursor.execute("commit");

        Messagebox.showinfo("INSERT STATUS","Inserted Successfully")
        con.close()

text_field1=Text(root)
name=Label(root,text="Name",font=("times new roman",20,"bold"),fg="blue").place(x=30,y=55)
text_field1.place(x=250,y=50,width=400,height=50)

text_field2=Text(root)
contact=Label(root,text="Contact Number",font=("times new roman",20,"bold"),fg="blue").place(x=30,y=155)
text_field2.place(x=250,y=150,width=400,height=50)

text_field3=Text(root)
age=Label(root,text="Age",font=("times new roman",20,"bold"),fg="blue").place(x=30,y=255)
text_field3.place(x=250,y=250,width=400,height=50)

but=Button(root,text="INSERT",font=("times new roman",12,"bold"),padx=40,pady=10,bg="pink",fg="blue",activebackground="pink",activeforeground="white",cursor="hand2",command=add).place(x=350,y=350)

root.mainloop()