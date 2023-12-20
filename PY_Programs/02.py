# Write programs to understand the use of Python String, Tuple, List, Set, Dictionary, File input/output

# String manipulation
my_string = "Hello, World!"

# Accessing characters in a string
print("First character:", my_string[0])
print("Last character:", my_string[-1])

# String slicing
print("Sliced string:", my_string[1:5])

# String concatenation
new_string = my_string + " How are you?"
print("Concatenated string:", new_string)

# String length
print("Length of the string:", len(my_string))

# String methods
print("Uppercase:", my_string.upper())
print("Lowercase:", my_string.lower())
print("Split string:", my_string.split(','))




# Tuple creation
my_tuple = (1, 2, 3, 'a', 'b', 'c')

# Accessing elements in a tuple
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Tuple slicing
print("Sliced tuple:", my_tuple[2:5])

# Tuple length
print("Length of the tuple:", len(my_tuple))





# List creation
my_list = [1, 2, 3, 'a', 'b', 'c']

# Accessing elements in a list
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# List slicing
print("Sliced list:", my_list[2:5])

# List length
print("Length of the list:", len(my_list))

# List methods
my_list.append('d')  # Adding an element to the list
print("Appended list:", my_list)

my_list.remove(2)  # Removing an element from the list
print("List after removal:", my_list)





# Set creation
my_set = {1, 2, 3, 4, 5}

# Accessing elements in a set
# Sets are unordered, so you can't access elements by index

# Adding elements to a set
my_set.add(6)
print("Set after addition:", my_set)

# Removing elements from a set
my_set.remove(3)
print("Set after removal:", my_set)




# Dictionary creation
my_dict = {'name': 'Alice', 'age': 25, 'country': 'USA'}

# Accessing values in a dictionary
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])

# Adding a new key-value pair to the dictionary
my_dict['city'] = 'New York'
print("Dictionary after addition:", my_dict)

# Removing a key-value pair from the dictionary
del my_dict['age']
print("Dictionary after deletion:", my_dict)



# Writing to a file
with open('example.txt', 'w') as file:
    file.write("This is an example file.\n")
    file.write("It contains some text.\n")

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print("File Content:")
    print(content)
