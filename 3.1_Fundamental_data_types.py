# Four types of number system available integer :
# Decimal Number System

a= 10
print(a)
print(a,type(a))

# Binary Number System

a = 0b010101 
print(a)
print(a,type(a))

a = 0B0000101011
print(a)
print(a,type(a))

b=21
c = bin(b)
print(c)

# Octal Number System

a= 0o11
print(a)
print(a,type(a))

b= 9
c = oct(b)
print(c)

# Hexadecimal Number System
a= 0x1A1
print(a)
print(a,type(a))

b= 417 
c = hex(b)
print(c)


a= 0X1A11
print(a)
print(a,type(a))



#Float DataType
###############################

a=12.44
print(a)

b= 23e02
print(b)

c= 43e-04
print(c)

# Bool
#############################

a=True
b=False
print(a,type(a))
print(b,type(b))

print(0b1111 * b - 0XF)


# Complex 
############################
# Complex number format  : a+bj  /  a-bj 
# a is the real part & b is the  imaginary part 
# j = sqrt(-1)

a= 2+3j
print(a)

b= 2-5j
print(b,type(b))

print(a.real)
print(b.imag)


