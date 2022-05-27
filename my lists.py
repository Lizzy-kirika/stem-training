my_list=[2,3,4,5,6,7,8,9,10]
for elem in my_list :
    print(elem)
other_list=[]
for elem in my_list:
    other_list.append(2)
    other_list.append(3)
    other_list.append(4)
    other_list.append(5)
    other_list.append(6)
    other_list.append(7)
    other_list.append(8)
    other_list.append(9)
    other_list.append(10)
print(other_list)

my_list=[2,3,4,5,6,7,8,9,10]
other_list=[elem for elem in my_list]
print(other_list)
for elem in my_list:
    if elem %2 ==0:
        other_list.append(elem)
print(other_list)
my_list=[2,3,4,5,6,7,8,9,10]
other_list=[elem for elem in my_list if elem %2==0]
print(other_list)


