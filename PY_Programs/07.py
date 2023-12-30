# Write programs to understand the use of Pandas Functions by Element, Functions by Row or Column, Statistics Functions, Sorting and Ranking, Correlation and Covariance, “Not a Number” Data.
import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Functions by Element
# Square each element
element_wise_square = df.applymap(lambda x: x**2)
print("\nElement-wise Square:")
print(element_wise_square)

# Functions by Row or Column
# Sum by column
sum_column = df.sum()
print(sum_column)

# Sum by row
sum_row = df.sum(axis=1)
print(sum_row)

# Statistical functions
print(df.describe())

print(df['A'].mean())

print(df['A'].median())

print(df['A'].mode())

print(df['A'].count())

# Sorting
# Sort by values in column 'B'
sorted_df = df.sort_values(by='B', ascending=False)
print("\nSorted DataFrame by Column 'B':")
print(sorted_df)

# Ranking
# Rank values in column 'C'
df['C_rank'] = df['C'].rank(ascending=False)
print("\nRanking of values in Column 'C':")
print(df)

# Correlation and Covariance
# Creating another DataFrame
data2 = {
    'X': [1, 2, 3],
    'Y': [40, 50, 60],
    'Z': [7, 8, 9]
}
df2 = pd.DataFrame(data2)
print("\nSecond DataFrame:")
print(df2)

# Correlation between columns
correlation = df2.corr()
print("\nCorrelation between Columns:")
print(correlation)

# Covariance between columns
covariance = df2.cov()
print("\nCovariance between Columns:")
print(covariance)

# Handling NaN (Not a Number) Data
# Introducing NaN in DataFrame
df2.loc[1, 'Y'] = pd.NA
df2.loc[2, 'Z'] = pd.NA
print("\nDataFrame with NaN:")
print(df2)

# Checking for NaN values
nan_values = df2.isna()
print("\nNaN Values:")
print(nan_values)
