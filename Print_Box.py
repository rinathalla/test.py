"""How to print below box

*****************
*               *
*               *
*               *
*****************

"""

def boxPrint(symbol,width,height):    #to print box pattern
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2))+ symbol)

    print(symbol * width)

boxPrint('*',15,5)
