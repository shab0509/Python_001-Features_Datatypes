# Set Datatypes
# is to store multiple values either of the same type of different type or both with unique values.
# Element of the set must be written within curly braces {} and seprated by comma.
# syntax to create an empty set :   setobj=set()
# An object does not maintain insertion order coz PVM can display any possibility of set object element.
# Can't perform Indexing/Slicing and set does not maintain insertion order.
# An object of set belongs to immutable(as set does not support item assignment) and mutable (in case of the ADD())

S1 = {10,20,30,50,60,10,30}
print(S1,type(S1))
S1.add("element_add")
print(S1)


# Operations on set
###############################

# 1. add()
# Used to add element to set object.

S1 = {10, "Python"}
print(S1,type(S1))

S1.add("Sagar")
print(S1)


# 2. clear()
# Used to remove all element from set object.

S1 = {10, "Python"}
print(S1,type(S1))
S1.clear()
print(S1)


# 3. remove()
# Used to remove specific element from set object.

S1 = {10, "Python", "Ram", "Pushpa"}
print(S1,type(S1))
S1.remove(10)
print(S1)


# 4. discard()
# Used to remove specific element from set object.
# If the element does not exist in set then no error at runtime.

S1 = {10, "Python", "Ram", "Pushpa"}
print(S1,type(S1))
S1.discard("Python")
print(S1)

# 5. pop()
# Used to remove any random element from set object.
 
S1 = {10, "Python", "Ram", "Pushpa",23.3,4565}
print(S1,type(S1))
S1.pop()
print(S1)

# 6. copy()
# Used to copy object from one set to another.
# Two types of copy(Shallow/Deep) 

# 1. Shallow Copy 
#########################
S1 = {10, "Python", "Ram", "Pushpa",23.3,4565}
print(S1,type(S1),id(S1))

S2= S1.copy()

print(S2,type(S2),id(S2))
 
# 1. Deep Copy 
#########################
S3 = {10, "Python", "Ram", "Pushpa",23.3,4565}
print(S3,type(S3),id(S3))

S4= S3 
print(S4,type(S4),id(S4))


# 7. isdisjoint()

# returns True provided both the set does not contain common elements
# returns False provided both the set contain common elements

S1= {10,20,30,40,50,60}
S2 = {10,20}
S3= S1.isdisjoint(S2)
print(S3)

# 8. issubset()

# returns true provided all element off set1 present in set2 otherwise false.
 
S1= {10,20,30,40,50,60}
S2 = {10,20}
S3= S2.issubset(S1)
print(S3)

 # 9. issuperset()

# returns true provided all element of set2 present in set1 otherwise false.
 
S1= {10,20,30,40,50,60}
S2 = {10,20}
S3= S1.issuperset(S2)
print(S3)

# 10. intersection
# obtains all the common element from both the set.

S1= {10,20,30,40,50,60}
S2 = {10,20}
S3= S1.intersection(S2)
print(S3)

# 11. difference
# removes all the common element from both sets.

S1= {10,20,30,40,50,60}
S2 = {10,20}
S3= S1.difference(S2)
print(S3)

#Note : many other function are available pls check at the time of practice.


# Frozenset

# Frozenset is used to store multiple values either of the same type or different type or both type with unique values.
# Element of frozenset can be obtained by converting othe type collection element by using froszenset().

# Frozenset does not maintain insertion order
# cannot perform indexing/slicing
# an onject of frozenset is immutable.

# Note : The functionality of frozenset is exactly similar to set but 
# frozenset object belongs to immutable and 
# set object belongs to mutable



s1 = {10,20,30,40}
print(s1,type(s1))

fs = frozenset(s1)
print(fs,type(fs))


t =(10,20,30,50,506,849,65,652)
print(t,type(t))

fs_001= frozenset(t)
print(fs_001,type(fs_001))

L1 =[10,20,30,50,506,849,65,652]
print(L1,type(L1))

fs_002= frozenset(L1)
print(fs_002,type(fs_002))

# Function available in Frozenset
# union,intersection,difference,symmnetric_difference,issuperset,issubset,isdisjoint




