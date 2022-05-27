fruit={"orange" , "mango" ,"apples"}
print(fruit)
print(fruit)
print(fruit)

def outputname(a):
    print("hi" ,a)
outputname("shee")

# function to replace characters in a string
def replace_in(phrase):
    word=""
    for letter in phrase :
        if letter.lower() in "aeiou" :
            word= word + "g"
        else:
            word = word + letter
    return word
print(replace_in(input("Enter a phrase :"))) 