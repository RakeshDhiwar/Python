"""
Key properties of dictionaries:
    Dictionaries are mutable
    Keys must be unique and immutable
    Values can be duplicated
    Useful methods like keys(), values(), clear()
"""

# Create dictionary
student = {
  'name': 'John',
  'age': 20,
  'courses': ['Math', 'Science']
}

# Access element  
print(student['name']) # John

# Update element
student['age'] = 21 

# Add new key-value pair  
student['phone'] = '555-1234'  

# Iterate over keys 
for key in student:
  print(key)

# Iterate over values
for value in student.values():
  print(value) 

# Check if key exists
print('name' in student) # True

# Length of dictionary
print(len(student)) # 4

# Get all keys 
print(student.keys()) 

# Get all values
print(student.values())

# Clear dictionary
student.clear()