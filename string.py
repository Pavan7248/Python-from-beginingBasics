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
#escape characters
#To insert characters that are illegal in a string, use an escape character.
#An escape character is a backslash \ followed by the character you want to insert.
#An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
#You will get an error if you use double quotes inside a string that is surrounded by double quotes:
#txt = "We are the so-called "Vikings" from the north."
#print(txt)
#The fix is to use the other quote character:
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
#You will also get an error if you use single quotes inside a string that is surrounded by single quotes:
#txt = 'We are the so-called 'Vikings' from the north.'
#print(txt)
#The fix is to use the other quote character:
txt = 'We are the so-called "Vikings" from the north.'
print(txt)
#Python has a set of built-in methods that you can use on strings.
#capitalize()	Converts the first character to upper case
#casefold()	Converts string into lower case
#center()	Returns a centered string
#count()	Returns the number of times a specified value occurs in a string
#encode()	Returns an encoded version of the string
#endswith()	Returns true if the string ends with the specified value
#expandtabs()	Sets the tab size of the string
#find()	Searches the string for a specified value and returns the position of where it was found
#format()	Formats specified values in a string
#format_map()	Formats specified values in a string
#index()	Searches the string for a specified value and returns the position of where it was found
#isalnum()	Returns True if all characters in the string are alphanumeric
#isalpha()	Returns True if all characters in the string are in the alphabet
#isdecimal()	Returns True if all characters in the string are decimals
#isdigit()	Returns True if all characters in the string are digits
#isidentifier()	Returns True if the string is an identifier
#islower()	Returns True if all characters in the string are lower case
#isnumeric()	Returns True if all characters in the string are numeric
#isprintable()	Returns True if all characters in the string are printable
#isspace()	Returns True if all characters in the string are whitespaces
#istitle()	Returns True if the string follows the rules of a title
#isupper()	Returns True if all characters in the string are upper case  
#join()	Joins the elements of an iterable to the end of the string
#ljust()	Returns a left justified version of the string  
#lower()	Converts a string into lower case
#lstrip()	Returns a left trim version of the string
#maketrans()	Returns a translation table to be used in translations

#partition()	Returns a tuple where the string is parted into three parts
#replace()	Returns a string where a specified value is replaced with a specified value
#rfind()	Searches the string for a specified value and returns the last position of where it was found
#rindex()	Searches the string for a specified value and returns the last position of where it was found
#rjust()	Returns a right justified version of the string
#rpartition()	Returns a tuple where the string is parted into three parts
#rsplit()	Splits the string at the specified separator, and returns a list

















