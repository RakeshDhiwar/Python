#Write programs to understand the use of Matplotlib for Simple Interactive Chart, Set the Properties of the Plot,matplotlib and NumPy
import matplotlib.pyplot as plt

# Basic interactive plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure()
plt.plot(x, y, marker='o')  # Line plot with markers
plt.title('Interactive Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)  # Enable grid
plt.show()

# Customizing plot properties
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 20]

plt.figure()
plt.scatter(x, y, color='red', marker='^', s=100, label='Data Points')  # Scatter plot with customized properties
plt.title('Customized Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()  # Show legend
plt.grid(True)
plt.show()

import numpy as np

# Generating data using NumPy
x = np.linspace(0, 10, 100)  # Generate 100 evenly spaced values from 0 to 10
y = np.sin(x)  # Calculate sine values for each x

plt.figure()
plt.plot(x, y, linestyle='--', color='green', label='Sin Wave')  # Line plot with sine values
plt.title('Sine Wave Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()
