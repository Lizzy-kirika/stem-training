"""
create one function (and run it)that
does the following:
-For a range of integers
between 0 and n (inclusive)
if the number is an even number,
half it 
if the number is an odd number,
double it
-For the output generated in the previous function,write the results to a file .Name the file"results.txt"
"""

def print_nums(n):
    for num in range (n):
        print(num)

print_nums(10)

x=0
while x<=25:
    if x % 5 ==0 and x % 3 ==0:
        print("half it")

    elif x % 3 ==0:
        print("half it")

    elif x % 5 ==0:
        print("double it") 
    x+=1




