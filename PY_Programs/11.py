# Write programs to understand the use of Matplotlib for Working with Line Chart, Histogram, Bar Chart, Pie Charts.

import matplotlib.pyplot as plt

# Line chart
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure()
plt.plot(x, y, marker='o')  # Line plot with markers
plt.title('Line Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

import numpy as np

# Histogram
data = np.random.randn(1000)  # Generating random data
plt.figure()
plt.hist(data, bins=30, color='skyblue', edgecolor='black')  # Histogram with specified bins and colors
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Bar chart
categories = ['A', 'B', 'C', 'D']
values = [7, 5, 10, 8]

plt.figure()
plt.bar(categories, values, color='orange')  # Bar chart
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid(axis='y')  # Grid along the y-axis
plt.show()

# Pie chart
labels = ['A', 'B', 'C', 'D']
sizes = [30, 20, 25, 25]
explode = (0, 0.1, 0, 0)  # Explode a slice for emphasis (here, the second slice 'B')

plt.figure()
plt.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', startangle=90)  # Pie chart with percentage display
plt.title('Pie Chart')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()
