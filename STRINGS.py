#String
print("Hi this is a good day to learn python")
print("This is going good")
print("I am learning python's named after monty python circus show")
print('This is to show that "quotes","single quotes","Double Quotes" can be played around')


#Passing String via inputs
#name = input("Pls enter ur name")
#surname = input("Pls enter your surname")

#Passing String in Variables
name = "Shabi"
Surname = " Victor"
print(name + Surname)

#Using double quotes in string
print("""Shabi is learning "split string within the" lines""" )

#Using \n & \t in string (ESCAPE chqarecters)
splitstring_newline= "This \nis \nnewline \nexample"
splitstring_tab ="This \tis \tto \tshow \ttab \tfunction"
print(splitstring_newline)
print(splitstring_tab)

#how to remove /t or /n as regular expression
#print("//Users//shabivictor//desktop//tsampletext.txt")
#print(r"//Users//shabivictor//desktop//sampletext.txt")

# Display the variable datatype(Assigned Dynamically)
name = 23424
print(type(name))

#Operator Precedence
#BODMAS = BRACEKTS,ORDER,DIVISION/MULTIPLICATION,ADDITION/SUBTRACTION
#Division & Multiplication have equal precedence.
#Addition & Subtraction have equal precedence.
# In case of equal precedence they are evaluated from left to right.

a = 9
b = 36
print(a+b)
c = a+b
d = b*3
e = d-3
print((a+b)/3 - 4*10)
print(a + b / 3 - 4*10)


