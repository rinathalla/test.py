from tkinter import *
from tkinter import  messagebox


def MessageBox():
    messagebox._show("Dialog Box","You have succesfully logged in")

def labeltext():
    labeltext.entry.set("Label")

root=Tk()

entry = Entry(root, bg='LightGrey', fg='black')
entry.pack()
entry2=Entry(root,bg='LightGrey', fg='black')
entry2.pack()
button=Button(root,text="Login",command=MessageBox).pack()
label=Label(root,textvariable="")

root.mainloop()