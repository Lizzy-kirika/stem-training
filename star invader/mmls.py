def print_nums(n):
    for num in range (n):
        print(num)

print_nums(10)

x=0
while x<=25:
    if x % 5 ==0 and x % 3 ==0:
        print("foobar")
    elif x % 3 ==0:
        print("foo")
    elif x % 5 ==0:
        print("bar")
    else:
        print(x)
    x+=1