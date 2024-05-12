a = "Hello World"
#everything inside single or double quotes is string
print(a)
#string is a collection of characters

#can use quotes inside a string, as long as they #don't match the quotes surrounding the string

b = "We are the so-called \"Vikings\" from the north."
print(b)

#can assign a multiline string to a variable by using three quotes

c = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(c)
#can access characters in a string by using its index

#strings are arrays.
#we can use functions in array to get position of characters.

#looping through a string

for x in "banana":
  print(x)


#to get the length of a string, use the len() function.
a = "Hello, World!"
print(len(a))

#check string
#to check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)

#use it in an if statement
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#check if not
txt = "The best things in life are free!"
print("expensive" not in txt)
#use it in an if statement
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


#String slicing
#you can return a range of characters by using the slice syntax.

#specify the start index and the end index, #separated by a colon, to return a part of the
#string.  
x = "Hello, World!"
print(x[1])
#slice from the start
print(x[:5])
#slice to the end
print(x[2:])
#negative indexing
#use negative indexes to start the slice from the end of the string
print(x[-5:-2])
#modify strings
#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())
#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())
#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip())
#replace strings
#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))
#split strings
#The split() method returns a list where the text between the specified separator becomes the list items.
a = "Hello, World!"
print(a.split(","))
#string concatenation
#To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"

c = a + b
print(c)
#To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#format strings
#You can combine strings and numbers by using the format() method!
age = 36


txt = "My name is John, and I am {}"
print(txt.format(age))
#You can add parameters inside the curly brackets to specify how to convert the argument to the string:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}"
print(myorder.format(quantity, itemno, price))










