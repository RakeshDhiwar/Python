"""
We can append, insert, extend to add elements

del, remove, pop are used to delete elements

Lists can be indexed and sliced like strings

len() gives the length

for loops can iterate over lists
"""
# Create a list 
fruits = ['apple', 'banana', 'orange']

# Access element at index
print(fruits[0]) # 'apple'

# Change element at index
fruits[1] = 'mango' 
print(fruits) # ['apple', 'mango', 'orange']

# List slicing
print(fruits[1:3]) # ['mango', 'orange'] 

# Check if element exists
print('apple' in fruits) # True

# Iterate over list
for fruit in fruits:
  print(fruit) 

# Length of list
print(len(fruits)) # 3

# Add element to list
fruits.append('grapes') 

# Insert element at index
fruits.insert(1, 'cherry')

# Remove element 
fruits.remove('cherry') 

# Delete element at index  
del fruits[0] 

# Sort list
fruits.sort()