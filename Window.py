from tkinter import *
from tkinter import messagebox

def buttonTapped():
    messagebox._show("Message","Button Clicked")

root = Tk()

Entry(root,text="").pack()
Button(root,text="Click",command=buttonTapped).pack()

root.mainloop()
