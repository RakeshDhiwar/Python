# Strings in Python

# Creating a string
str1 = "Hello"
str2 = 'World'

# String concatenation
str3 = str1 + " " + str2 

# String indexing 
print(str3[0]) # H

# String slicing
print(str3[2:5]) # llo

# String length
print(len(str3)) # 10

# String methods
print(str3.upper()) # HELLO WORLD
print(str3.lower()) # hello world
print(str3.title()) # Hello World
print(str3.count('l')) # 3

# Formatting strings 
name = "Rakesh"
print(f"Hello {name}") # Hello RAkesh
print("Hello {}".format(name)) # Hello Rakesh

# Raw strings
print(r"This prints \n as is") # This prints \n as is

"""
Strings can be created with '' or ""
'+' operator concatenates strings
Indexing and slicing accesses characters
len() gives length of string
Methods like upper(), lower() manipulate the string
f-strings and str.format() allow formatting
Raw strings ignore escape characters
"""