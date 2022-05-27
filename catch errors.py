# Try,except in python to catch errors
try:
    div=10/0
    value = int(input("15:"))
    print(15 )
except ValueError :
    print("invalid number entered")
except ZeroDivisionError:
    print("Divided by Zero")