def div45by(divideBy):
    try:
        return  45/divideBy
    except ZeroDivisionError:
        print("Error:you tried to divide by zero:")

print(div45by(5))
print(div45by(16))
print(div45by(0))
print(div45by(1))
