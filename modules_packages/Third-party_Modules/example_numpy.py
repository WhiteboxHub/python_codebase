import numpy as np

# Create a 1D numpy array
arr = np.array([1, 2, 3, 4, 5])
print(arr)  # Output: [1 2 3 4 5]

# Perform element-wise operations
arr_squared = np.square(arr)
print(arr_squared)  # Output: [ 1  4  9 16 25]

# Create a 2D array (matrix)
matrix = np.array([[1, 2], [3, 4]])
print(matrix)
# Output:
# [[1 2]
#  [3 4]]

# Perform matrix multiplication
result = np.dot(matrix, matrix)
print(result)
# Output:
# [[ 7 10]
#  [15 22]]
