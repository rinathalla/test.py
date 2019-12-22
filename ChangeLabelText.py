from tkinter import *


def onButtonClick():
    labelText.set('text changed on button click')


root = Tk()

labelText = StringVar()
labelText.set('label')

label = Label(root, textvariable=labelText)
label.pack()
Button(root, text="Click", command=onButtonClick).pack()
root.mainloop()
