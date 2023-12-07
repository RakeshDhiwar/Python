"""
Tuples are created with () instead of []

Elements can be accessed by index

Tuples are immutable - elements can't be modified

We can iterate over tuples like lists


Use in to check if a value exists

Indexing and slicing works like lists

len() gives the length

tuple() converts a list to a tuple

list() converts a tuple to a list

The key difference between tuples and lists is that tuples are immutable.
"""

# Tuple packing
fruits = ('apple', 'banana', 'mango')

# Tuple unpacking
(green, yellow, orange) = fruits

print(green) # 'apple'
print(yellow) # 'banana' 
print(orange) # 'mango'

# Nested tuple
basket = ('apple', 'banana', ('grapes', 'orange'))

# Access nested element
print(basket[2][1]) # 'orange' 

# Tuple without parentheses 
languages = 'Python', 'Java', 'C++'  



# Concatenate tuples
numbers = (1, 2) + (3, 4) 
print(numbers) # (1, 2, 3, 4)

# Count number of elements
print(fruits.count('apple')) # 1

# Return index of value
print(fruits.index('banana')) # 1

#Updating tuples using list() and tuple()
fruits = ('apple', 'banana', 'mango')
print(fruits)
newlist = list(fruits)
newlist[1] = "mango"
fruits=tuple(newlist)
print(fruits)

