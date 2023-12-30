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


# Creating a Series with custom index
data = [10, 20, 30, 40]
index = ['A', 'B', 'C', 'D']
series = pd.Series(data, index=index)
print(series)



data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}

df = pd.DataFrame(data)
print("\nOriginal DataFrame:")
print(df)
# Reindexing
new_index = ['X', 'Y', 'Z']
reindexed_df = df.reindex(new_index)
print("\nReindexed DataFrame:")
print(reindexed_df)

# Dropping columns
columns_dropped = reindexed_df.drop('C', axis=1)
print("\nDataFrame after dropping 'C' column:")
print(columns_dropped)

# Arithmetic operations
df_1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df_2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})

# Addition
added_df = df_1 + df_2
print("\nAdded DataFrames:")
print(added_df)

# Subtraction
subtracted_df = df_2 - df_1
print("\nSubtracted DataFrames:")
print(subtracted_df)

#Data Alignment
s1 = pd.Series([10,20,30], index=['A','B','c'])
s2 = pd.Series([15,10,50], index=['B','C','D'])
print(s1+s2)