from tkinter import *
root=Tk()
root.title("form")
root.geometry("500x500+0+0")
def show_text():
    if checkvar.get()==1:
        result1 = "Name : "+ text_field.get('1.0',END) +"Gender : "+ gendervar.get()
        result.config(text=str(result1))
    else:
        result.config(text="Accept")


    


text_field=Text(root)
name=Label(root,text="Enter Name",font=("times new roman",20,"bold"),fg="blue").place(x=30,y=55)
text_field.place(x=250,y=50,width=200,height=50)


gendervar=StringVar()
gender=Label(root,text="Select Gender",font=("times new roman",20,"bold"),fg="blue").place(x=30,y=205)
radiob1=Radiobutton(root,font=("times new roman",20,"bold"),value="Female",variable=gendervar).place(x=250,y=200)
l1=Label(root,text="F").place(x=252,y=230)
radiob2=Radiobutton(root,font=("times new roman",20,"bold"),value="Male",variable=gendervar).place(x=300,y=200)
l2=Label(root,text="M").place(x=302,y=230)
radiob3=Radiobutton(root,font=("times new roman",20,"bold"),value="Transgender",variable=gendervar).place(x=350,y=200)
l3=Label(root,text="T").place(x=352,y=230)
gendervar.set("Female")


checkvar=IntVar()
checkb=Checkbutton(root,text="Accept",font=("times new roman",15,"bold"),onvalue=1,offvalue=0,variable=checkvar).place(x=250,y=300)
checkvar.set(1)
result=Label(root,text="")
result.place(x=0,y=350,relwidth=1)
but=Button(root,text="Show",padx=40,pady=10,bg="pink",fg="blue",activebackground="pink",activeforeground="white",cursor="hand2",command=show_text).place(x=200,y=450)
root.mainloop()
