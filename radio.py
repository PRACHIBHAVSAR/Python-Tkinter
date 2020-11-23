from tkinter import *
root=Tk()
root.title("radio")
root.geometry("800x500+0+0")
def show():
    print(gender.get())
gender=Label(root,text="Select gender",font=("times new roman",20,"bold"),bg="pink",fg="blue").place(x=100,y=50)

gender=StringVar()

male=Radiobutton(root,text="MALE",value="male",variable=gender).place(x=300,y=60)
female=Radiobutton(root,text="FEMALE",value="female",variable=gender).place(x=450,y=60)
transgender=Radiobutton(root,text="TRANSGENDER",value="transgender",variable=gender).place(x=600,y=60)
gender.set("female")
show_data=Button(root,text="SHOW",font=("times new roman",20,"bold"),bg="pink",fg="blue",command=show).place(x=400,y=250)

root.mainloop()