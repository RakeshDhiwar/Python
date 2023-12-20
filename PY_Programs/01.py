# Write programs to understand the use of Python Identifiers, Keywords, Indentations, Comments in Python, Operators, Membership operator

# Identifiers
variable_name = 10
another_variable = "Hello, World!"

# Keywords (This code demonstrates a few Python keywords)
import keyword
all_keywords = keyword.kwlist
print("Python Keywords:", all_keywords)

# Indentations
if variable_name > 5:
    print("Variable is greater than 5")
else:
    print("Variable is 5 or less")

# Comments
# This is a single-line comment
"""
This
is
a
multi-line
comment
"""

# Arithmetic Operators
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)

# Comparison Operators
print("Is a greater than b?", a > b)
print("Is a less than or equal to b?", a <= b)
print("Is a equal to b?", a == b)
print("Is a not equal to b?", a != b)

# Logical Operators
x = True
y = False
print("Logical AND:", x and y)
print("Logical OR:", x or y)
print("Logical NOT:", not x)

# Assignment Operators
c = 15
c += 5  # Equivalent to c = c + 5
print("Value of c after using +=:", c)

# Bitwise Operators
m = 10
n = 4
print("Bitwise AND:", m & n)
print("Bitwise OR:", m | n)
print("Bitwise XOR:", m ^ n)
print("Bitwise NOT:", ~m)
print("Bitwise Left Shift:", m << 2)
print("Bitwise Right Shift:", m >> 2)

my_list = [1, 2, 3, 4, 5]

# Using 'in' membership operator
if 3 in my_list:
    print("3 is present in the list")

# Using 'not in' membership operator
if 6 not in my_list:
    print("6 is not present in the list")
