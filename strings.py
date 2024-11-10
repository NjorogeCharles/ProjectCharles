from datatype import greeting
from variables import lastname

text = "Hello World"
course = "WEB DEVELOPMENT"
print(text)

#Accessing an element in a string
print(text[1])

#Size/Length of string
print(len(text))

#Modifying a string
print(course.lower())
print(text.upper())

#String Concatenation - joining strings
text = "Hello there"
firstname = "Charles"
space = " "

print(text + " " + firstname)
print( text+ space+ firstname)