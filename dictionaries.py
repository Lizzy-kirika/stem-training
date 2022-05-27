# Dictionaries in python
mydict ={
    "book" : "dynamics",
    "publisher": "longhorn",
    "year": 2001
}

# Accessing item
x=mydict["year"]
print(x)

# Accessing using get()
y= mydict.get("year")
print(y)

# All keys
x= mydict.keys()
print(x)

# All values
x=mydict.values()
print(x)

# Printing all items in a dictionary
x=mydict.items()
print(x)

# Checking if keys exist
if "Publisher" in mydict :
    print("publisher is one of the keys")
    print(len(mydict))

# Dictionaries can hold different data types
