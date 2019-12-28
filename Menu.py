from tkinter import *
from tkinter import messagebox

def ShowDialogBox():
    messagebox._show( "Dialog Box","Open is Clicked")

def quitApplication():
       quit()
root=Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu=Menu(menu,tearoff=0)
menu.add_cascade(label = 'File',menu = subMenu)
subMenu.add_command(label="Open",command=ShowDialogBox)
subMenu.add_command(label="Save")
subMenu.add_command(label="Quit",command=quitApplication)

subMenu2=Menu(menu,tearoff=0)
menu.add_cascade(label = 'Edit',menu = subMenu)
subMenu2.add_command(label="Cut")
subMenu2.add_command(label="Copy")
subMenu2.add_command(label="Paste")

subMenu3=Menu(menu,tearoff=0)
menu.add_cascade(label = 'View',menu = subMenu)
subMenu3.add_command(label="Tools Window")
subMenu3.add_command(label="Recent Files")
subMenu3.add_command(label="Recent Changes")

root.mainloop()