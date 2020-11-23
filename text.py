from tkinter import *
root=Tk()
root.title("bdjebj")
root.geometry("800x500+0+0")
def show_text():
    var.set(str(text_field.get('1.0',END)))
    print(var.get())


var=StringVar()
text_field=Text(root)
text_field.place(x=100,y=400,width=200,height=50)

but=Button(root,text="Submit",padx=20,pady=30,bg="grey",fg="white",activebackground="pink",activeforeground="white",cursor="hand2",command=show_text).place(x=400,y=150)
root.mainloop()
