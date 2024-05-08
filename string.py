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

