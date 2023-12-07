"""
Key properties of sets:
    Elements are unique
    Sets are unordered
    Common set operations like union, intersection, difference
"""

# Create a set
numbers = {1, 2, 3, 4}

# Add element 
numbers.add(5)

# Remove element
numbers.remove(3) 

# Iterate over set 
for n in numbers:
  print(n) 

# Check if element exists
print(1 in numbers) # True

# Length of set
print(len(numbers)) # 3

# Union of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1 | set2 # {1, 2, 3, 4, 5}

# Intersection 
set4 = set1 & set2 # {3}

# Difference  
set5 = set1 - set2 # {1, 2}

# Symmetric difference
set6 = set1 ^ set2 # {1, 2, 4, 5} 

# Clear set 
numbers.clear()