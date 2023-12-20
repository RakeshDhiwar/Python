# Write programs to understand the use of Numpy’s Structured Arrays, Reading and Writing Array Data on Files

import numpy as np

# Creating a structured array
data = np.array([(1, 'Alice', 25), (2, 'Bob', 30), (3, 'Charlie', 35)],
                dtype=[('id', int), ('name', 'U10'), ('age', int)])

print("Structured Array:")
print(data)

# Accessing structured array elements
print("\nFirst element's ID:", data['id'][0])
print("Second element's Name:", data['name'][1])
print("All ages:", data['age'])



# Writing array data to a file
np.save('data.npy', data)

# Reading array data from the file
loaded_data = np.load('data.npy')
print("\nLoaded Data from File:")
print(loaded_data)
