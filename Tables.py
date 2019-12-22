from tkinter import *

def showTable():
    table = entry.get()

    labelText1.set(table +  'x'  + '1 = ' + table)
    labelText2.set(table + 'x' + '2 = ' + table)
    labelText3.set(table + 'x' + '3 = ' + table)
    labelText4.set(table + 'x' + '4 = ' + table)
    labelText5.set(table + 'x' + '5 = ' + table)
    labelText6.set(table + 'x' + '6 = ' + table)
    labelText7.set(table + 'x' + '7 = ' + table)
    labelText8.set(table + 'x' + '8 = ' + table)
    labelText9.set(table + 'x' + '9 = ' + table)
    labelText10.set(table + 'x' + '10 = ' + table)

root = Tk()

entry = Entry(root)
entry.pack()


Button(root, text="Show table", command=showTable).pack()

labelText1 = StringVar()
labelText1.set('_________')
Label(root,textvariable=labelText1,bg="lightpink").pack()

labelText2 = StringVar()
labelText2.set('_________')
Label(root,textvariable=labelText2,bg="lightblue").pack()

labelText3 = StringVar()
labelText3.set('_________')
Label(root,textvariable=labelText3,bg="lightgreen").pack()


labelText4 = StringVar()
labelText4.set('_________')
Label(root,textvariable=labelText4,bg="lightyellow").pack()

labelText5 = StringVar()
labelText5.set('_________')
Label(root,textvariable=labelText5,bg="red").pack()

labelText6 = StringVar()
labelText6.set('_________')
Label(root,textvariable=labelText6,bg="pink").pack()

labelText7 = StringVar()
labelText7.set('_________')
Label(root,textvariable=labelText7,bg="royalblue").pack()

labelText8 = StringVar()
labelText8.set('_________')
Label(root,textvariable=labelText8,bg="grey").pack()

labelText9 = StringVar()
labelText9.set('_________')
Label(root,textvariable=labelText9,bg="yellow").pack()

labelText10 = StringVar()
labelText10.set('_________')
Label(root,textvariable=labelText10,bg="orange").pack()

root.mainloop()