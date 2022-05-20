#complex calculator
1.#ADD
2.#SUBTRACT
3.#MULTIPLY
4.#DIVIDE

print("select an operation to perfom:")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
operation=input()
num1=5
num2=2
print("num1")
print("num2")
if operation ==1:
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("The sum is " + num1 + num2)
     #code for add
elif operation ==2:
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("The sum is " + num1 - num2)
    #code for subtract
    
elif operation ==3:
    num1= input("Enter first number:")
    num2= input("Enter second number:")
    print("The sum is " + num1 * num2)
    #code for multiply

elif operation ==4:
    num1= input("Enter first number:")
    num2= input("Enter second number:")
    print("The sum is " + num1/num2)
    #code for division
else:
    print("invalid entry")
x=5
y=2
print(x+y)
print(x-y)
print(x*y)
print(x/y)





