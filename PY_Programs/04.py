# Write programs to understand the use of Numpy’s Shape Manipulation, Array Manipulation, Vectorization.

import numpy as np

# Creating an array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Reshaping the array
reshaped_arr = arr.reshape(3, 2)
print("Original array:\n", arr)
print("Reshaped array:\n", reshaped_arr)

# Flattening the array
flattened_arr = arr.flatten()
print("Flattened array:", flattened_arr)


# Concatenation
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])
concatenated_arr = np.concatenate((arr1, arr2), axis=0)
print("Concatenated array:\n", concatenated_arr)

# Splitting arrays
arr3 = np.array([1, 2, 3, 4, 5, 6])
split_arr = np.split(arr3, 3)
print("Split array:", split_arr)


# Performing operations on arrays without explicit looping
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise addition
addition = a + b
print("Element-wise addition:", addition)

# Element-wise multiplication
multiplication = a * b
print("Element-wise multiplication:", multiplication)

