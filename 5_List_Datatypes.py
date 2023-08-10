# List Data Types (Collection Datatypes)
# The Purpose of list datatype is to store multiple values either of the same type or different type or both type with unique & duplicate values.
# Element of the list must be written in square brackets and seprated by comma's.
# They are classified as two types   <List(Mutable) / Tuple(Immutable)>


# Types of List objects <Empty list / Non-Empty list>
# Empty list
L1 = []
print(L1,type(L1))
print(len(L1))

# Non-Empty list
L2 = ['a',123,'xyz']
print(L2,type(L2))
print(len(L2))

#List
#Operation on List : Index / Slicing
# Pre-defined Function in list : append() / insert() / clear() / remove() / pop(index) / pop / count() / index() / reverse() / sort() / copy() (Shallow/Deep)

# 1. APPEND() 
# Function used for adding data at the end of the list object.

L1 = [10,20,258,1000,-23,10,20]
print(L1)

L1.append(777)
print(L1)

# 2. INSERT() 
# Function used for inserting thew specified value at specific existing index.

L1 = ["Rossum", 10 , 45.67, True]
print(L1) 

L1.insert(3,"Inserted object")
print(L1)

# 3. CLEAR() 
# Function used for removing all the element of the list object.

L2 = [10,'ABC', 2+5j, True]
print(L2)
L2.clear()
print(L2)

# 4. REMOVE() 
# Function used for removing the first occurence of the specified list object.

L1 = [120,"Document",True ,23.54]
print(L1)

L1.remove(True)
print(L1)

# 5. POP(INDEX) 
# Function used for removing an element from specified index(+ve/-ve).

L1 = [120,"Document",True ,23.54]
print(L1)

L1.pop(1)
print(L1)

L1.pop(-2)
print(L1)


# 6. POP 
# Function used for removing the last element of the list object.

L2 = ["ABC",123.4322,True,22]
print(L2)

L2.pop()
print(L2)

L2.pop()
print(L2)


 # 7. CLEAR  
# Function used for counting the number of occurences of specific list object.

L2 = ["ABC",123.4322,True,22,True]
print(L2.count(True))

# 8. Reverse

L1 = [122, 34.6, 'pagal dunia', False]
print(L1)
L1.reverse()
print(L1)

# 9. Copy (Shallow / Deep)

# Shallow Copy
# Initial content of the both the object are same.
# Memory address of the both the object are different.
# Both object modification are different.
# syntax:  L2 =L1.copy()

L1 = [10, "Rossum" , 'PYTHON' , 45.56 ,10 ]
print(L1)

L2 = L1.copy()
L2.append(232312)
print(L2)
 
# Deep Copy
# Initial content of the both the object are same.
# Memory address of the both the object are Same.
# Both object modification are independent.
# syntax:  L2=L1


L1 = ['ABC', "shabi" ,34.55, 3+3j]
print(L1)

L2 = L1
print(L2)

L2.append("New Element")
print(L2)
print(L1)


# Nested List
# List within a list is called Nested list.
# On the inner list, we can perform Indexing / Slicing / All methods of List

L1 = [10, "ROSSUM", [19,15,1,76], [89,90,91,92], "OUCET"]

print(L1)

print(L1[2][-2])
L1[2].append(23)
print(L1)

L1[2].sort(reverse= False)
print(L1)



# Tuple
# Is to store multiple values either of the same/different type with unique/different values.
# Element must be provided within braces ().
# Maintains Insertion order
# performs indexing & slicing
# To convert one type into tuple, we use tuple.

T1 = (23,345.344, "Abc")
T2 = (10,1000,90,70) 

print(T1)
print(T2)

L2 = tuple(T2)
print(L2)
