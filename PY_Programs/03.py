# Write programs to understand the use of Numpy’s Ndarray, Basic Operations, Indexing, Slicing, and Iterating, 
# Conditions and Boolean Arrays.


import numpy as np

# Creating ndarrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Basic operations
print("Array 1:", arr1)
print("Array 2:\n", arr2)

# Addition
print("Sum of arrays:\n", arr1 + arr2)

# Multiplication
print("Product of arrays:\n", arr1 * arr2)

# Transpose
print("Transposed array 2:\n", arr2.T)

# Indexing
print("Element at index 2 in arr1:", arr1[2])
print("Element at row 1, column 2 in arr2:", arr2[1, 2])

# Slicing
print("Sliced arr1:", arr1[1:3])
print("Sliced arr2:\n", arr2[:, 1:])

# Iterating through arrays
print("Iterating through arr2:")
for row in arr2:
    print(row)



# Conditions and boolean arrays
print("Elements greater than 3 in arr1:", arr1[arr1 > 3])

# Using boolean arrays as indices
bool_arr = np.array([True, False, True, False])
print("Elements at True positions in bool_arr:", arr1[bool_arr])

# Conditional assignment
arr1[arr1 > 2] = 10
print("Updated arr1:", arr1)
