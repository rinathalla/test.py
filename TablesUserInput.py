number = input ("Enter a Number : ")
for value in range(1,11):
    multiply= value * int(number)
    line= str(number) + "x" + str(value) + "=" + str(multiply)
    print(line)
