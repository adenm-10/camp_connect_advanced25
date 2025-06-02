import numpy as np

# Create arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Vectorized operations
sum_ab = a + b       # array([5, 7, 9])
dot = np.dot(a, b)   # 1*4 + 2*5 + 3*6 = 32

# Reshaping and statistics
matrix = np.array([[1, 2], [3, 4]])
mean_val = np.mean(matrix)  # 2.5
transposed = matrix.T       # [[1 3], [2 4]]
