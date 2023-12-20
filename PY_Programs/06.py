# Write programs to understand the use of Pandas Series, DataFrame, Index Objects, Reindexing, Dropping, Arithmetic and Data Alignment

import pandas as pd

# Creating a Pandas Series
data = pd.Series([10, 20, 30, 40], index=['A', 'B', 'C', 'D'])
print("Pandas Series:")
print(data)

# Accessing elements of a Series
print("\nValue at index 'B':", data['B'])
print("Values greater than 20:")
print(data[data > 20])

