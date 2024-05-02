#F-string allows you to embed expressions inside string literals, using a minimal syntax
#to specify the stringas a f-string ,simply prefix the string with the letter f.

txt = f"The price is 49 dollars"
print(txt)
# Modifiers and Placeholders
# The f-string allows you to embed expressions inside 
 # string literals, using a minimal syntax to specify the 
 #string as a f-string, simply prefix the string with the letter f.

price = 59
txt = f"The price is {price} dollars"
print(txt)

#A modifier can be used to format the output of the f-string.
#A modifier is included by adding a colon : followed by a 
 #legal formatting type, like .2f which means fixed point number with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#perform operations in f-string

txt = f"The price is {20 * 59} dollars"
print(txt)
#A placeholder is used to define the type of data that will be passed into the f-string.
price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

#can perform if-else in f-string
price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt)

#can execute functions in f-string
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)
