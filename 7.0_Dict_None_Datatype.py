# Dict Datatype
# Purpose of dict datatype is to store data in the form of (Key,Value)
# In (Key, Value)  the value of key represents unique value and the value of Value may or may not be unique.
# Syntax :  dictobj = {key1:val1, key2:val2}
# If we use any values for keys of str type then they must be enclosed within single/double quotes.
# Object of dict maintain insertion order.
# Values of keys are immutable and values of Value are mutable.
# Two types of dict objects :   Empty Dict / Non-Empty Dict

d1={}
print(d1,type(d1))
d2 =dict(d1)
print(d2,type(d2))


d1[10]= "Shabi"
d1[20]= "Suman"
d1[30]= "Zayn"
print(d1)

# Functions available in dict objects
# clear/copy(shallow)/get/pop/popitem//keys/values/items/update



# None type datatype
####################################3

# "NoneType" is pre-defined class and treated as none datatype.
# "None" is keyword act as value for  <class,'NoneType'>
# Value of "None" is False, empty, 0
# An object of None data type can be created explicitly.
 
a = None
print(a,type(a))

#Use Case
def greet(name=None):
    if name == None:
        return "hello Stranger"
    return f"hello {name}"
print("Hey")
print(greet('Evaan'))







