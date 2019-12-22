from tkinter import *


def changeToRed():
    labelText.set('Red')
    label.config(bg='red')

def changeToGreen():
     labelText.set('Green')
     label.config(bg='green')

def changeToPink():
     labelText.set('Pink')
     label.config(bg='pink')

root = Tk()

labelText = StringVar()
labelText.set('label')

label = Label(root, textvariable=labelText)
label.pack()

Button(root, text="Red", command=changeToRed).pack()

Button(root, text="Green", command=changeToGreen).pack()

Button(root, text="Pink", command=changeToPink).pack()

root.mainloop()
