from tkinter import *
from tkinter import ttk

def ShowOnLabel():
    labelText.set(entry.get())


root = Tk()

entry = Entry(root, bg='pink', fg='black')
entry.pack()

labelText = StringVar()
labelText.set('-------------------')

label = Label(root, textvariable=labelText)
label.pack()

ttk.Button(root, text="Click", command=ShowOnLabel).pack()



root.mainloop()
