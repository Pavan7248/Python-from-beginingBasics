#Type Casting is the method to convert the Python variable 
#datatype into a certain data type in order to perform the #required operation by users.
#There can be two types of Type Casting in Python:

#Python Implicit Type Conversion
#Python Explicit Type Conversion

#Implicit Type Casting: Python converts the datatype into another datatype automatically.
#Users don’t have to involve in this process. 

# Python program to demonstrate 
# implicit type Casting 

# Python automatically converts 
# a to int 
a = 7
print(type(a)) 

# Python automatically converts 
# b to float 
b = 3.0
print(type(b)) 

# Python automatically converts 
# c to float as it is a float addition 
c = a + b 
print(c) 
print(type(c))

# Python automatically converts 
# d to float as it is a float multiplication
d = a * b
print(d)
print(type(d))

#Explicit Type Casting: User has to involve in this process.
#Mainly type casting can be done with these data type functions:

#Int(): Python Int() function take float or string as an argument and returns int type object.
#float(): Python float() function take int or string as an argument and return float type object.
#str(): Python str() function takes float or int as an #argument and returns string type object.

# Python program to demonstrate 
# type Casting 

# int variable
a = 5

# typecast to float
n = float(a)

print(n)
print(type(n))
