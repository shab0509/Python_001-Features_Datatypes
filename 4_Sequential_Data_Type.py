# Sequential Data Types
# [STRING / BYTES / BYTEARRAY / RANGE]


# 1.String
############################
#Purpose of 'str' data types is to store string datatype.
#Operation on string :  indexing(Positive/Negative) , Slicing
#Organisation of string : Single Line str data  >> " " , ' '
#                       : Multiple line str data  >> """ """ , ''' '''

a ="Shabi has started working on things"
print(a)

b = 'Hi shabi'
print(b)

c = """Hi this world is not fair immediately 
but someday it will turn out to be fair 
that is the mystery which this world beholds"""
print(c)

d= '''Hello
Hi''' 
print(d)


# Indexing
###########################

S = 'PYTHON'
print(S)
print(S[0])
print(S[5]) 

print(S[-1])
print(S[-4])


# Slicing
###########################
S = 'PYTHON'
print(S)

print(S[0])
print(S[5]) 
print(S[-1])
print(S[-4])

#Slicing

print(S[0:3])   #Positive Slicing
print(S[:3])

print(S[-4:-1]) #Neagtive Slicing 
print(S[:-2])


# 2.Bytes
############################
# It is used for storing sequence of numerical integer value ranges from 0 to 256
# An object of Bytes datatype belongs to immutable.
# To represent the element of Bytes datatype, we dont have any symbolic notation but we can convert other type of element into Bytes using byte().
# On the object of Bytes, we can perform indexing & slicing.
# An oject of Bytes preserves insertion order.


l1 = [0,10,20,30,50,255]
print(l1,type(l1))

l2 = bytes(l1)
print(l2, type(l2))


for x in l2:
    print(x)

print(l2[2])  #indexing in Bytes


# 2. BYTEARRAY
############################

# used for storing sequence of numerical integer values ranges from 0 to 256.
# An object of Bytearray datatype belong to mutable.
# To represents the element of bytearray data type, we dont have any symbolic notation but we can convert other types of element into bytearray type by using bytearray().
# On the object of bytearray, we can perform indexing & slicing.
# Objects of bytearray preserves insertion order.

# Note : The functionality of Bytes and Bytearray is exactly similar but 
# an object of Bytes is immutable where as an object of bytearray is mutable.


t= [10,20,30,252]
print(t,type(t))

t1= bytearray(t)
print(t1,type(t1))
t1[2] =33        # mutability
print(t1,type(t1))


for x in t1:
    print(x)


# 2. RANGE
############################
# is used to  store numerical integer value with equal interval of values.
# An object of range belongs to immutable coz "object does not support item assignment"
# On the object of range , we can perform indexing & slicing 
# Range object maintain insertion order.

#  Syntax_001  varname = range(Value)
#  Syntax generates ranges from values 0 to value-1

r = range(4)
print(r,type(r))
for v in r :
    print(v)

# Syntax_002 varname = range(begin,end)

r1 = range(400,415)
print(r1,type(r1))

for v in r1:
    print(v)

# Syntax_003 varname = range(begin,end,step)

r2 = range(1,21,3)
print(r2,type(r2))

for v in r2:
    print(v)


# Syntax_003 Specail Case  

r3 = range(100,1040) [2:40]    
print(r3,type(r3))

for v in r3 :
    print(v)
