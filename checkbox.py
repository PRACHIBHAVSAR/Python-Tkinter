from tkinter import *
root=Tk()
root.title("radio")
root.geometry("800x500+0+0")
def showselected():
    print(checkvar.get())

checkvar=IntVar()
check=Checkbutton(root,text="Accept",font=("times new roman",20,"bold"),onvalue=1,offvalue=0,variable=checkvar).place(x=200,y=100)
checkvar.set(1)
show_data=Button(root,text="SHOW",font=("times new roman",20,"bold"),bg="pink",fg="blue",command=showselected).place(x=400,y=250)
root.mainloop()