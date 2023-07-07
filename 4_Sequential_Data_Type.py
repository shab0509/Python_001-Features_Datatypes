# Sequential Data Types
# [string/byte/bytearray/range]


# 1.String
############################
#Purpose of 'str' data types is to store string datatype.
#Operation on string :  indexing(Positive/Negative) , Slicing
# Organisation of string : Single Line str data  >> " " , ' '
#                        : Multiple line str data  >> """ """ , ''' '''

a ="Shabi has started working on things"
print(a)

b = 'Hi shabi '
print(b)

c = """Hi this world is not fair immedaitely 
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

print(S[-4:-1]) #Negative Slicing 
print(S[:-2])


