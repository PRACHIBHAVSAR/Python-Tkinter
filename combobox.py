from tkinter import *
from tkinter import ttk
root=Tk()
root.title("combo")
root.geometry("800x500+0+0")
def get_data():
    print(lang.get())
lang=ttk.Combobox(root,values=("CPP","JAva","python"),state='readonly')
lang.place(x=100,y=200)
lang.set("Select Language")
but=Button(root,text="show",command=get_data).place(x=400,y=400)
root.mainloop()