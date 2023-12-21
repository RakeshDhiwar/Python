
import numpy as np 

# # Creating ndarrays
# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# # Basic operations
# print("Array 1:", arr1)
# print("Array 2:\n", arr2)

# # Element-wise addition
# result_add = arr1 + 10
# print("Addition with scalar:", result_add)

# # Element-wise Subtraction
# result_sub = arr1 - 10
# print("Subtraction with scalar:", result_sub)

# # Element-wise multiplication
# result_mul = arr2 * 2
# print("Multiplication with scalar:\n", result_mul)

# Matrix multiplication
# arr3 = np.array([[1, 2], [3, 4]])
# arr4 = np.array([[5, 6], [7, 8]])
# result_matmul = np.matmul(arr3,arr4)
# result_matmul1 = np.dot(arr3,arr4)
# result_matmul2 = arr3.dot(arr4)
# print("Matrix multiplication:\n", result_matmul1)

# print(np.cross(arr3, arr4))

# arr = np.array([[1,2,3,1],[4,5,6,1]])
# print(arr.ndim) #dimension
# print(arr.shape) #rows and column
# print(arr.size)  #number of element
# print(arr.dtype)
# print(arr.itemsize)


# Indexing and slicing
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print("Original array:\n", arr)

# # Indexing
# print("Element at (1, 2):", arr[1, 2])
# print(arr[0,:])  #0th row
# print(arr[:,1])  #1st col

# # Slicing
# arr = np.array([10,20,30,40,50,60,70])
# print(arr[1:3])
# print(arr[1:6:2])
# print(arr[-1:-3:-1])
# print(arr[::2])
# print(arr[::-1]) #inverting

arr=np.array([[15,16,17],[25,26,27],[35,36,37],[45,46,47]])
print(arr[1:1])
print(arr[:,1])
print(arr[1:3,1:3])
print(arr[1:3, ])
print(arr[:,1:3])
print(arr)

# # Iterating through array elements
# print("Iterating through elements:")
# for row in arr:
#     for val in row:
#         print(val, end=' ')
#     print()
