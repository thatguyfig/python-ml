# You want to change the shape (number of rows and columns) of an array without changing the element values.

import numpy as np

# create 4x3 matrix
matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
])

# reshape matrix into 2x6 matrix
print("Original matrix: " + str(matrix))
print("Reshaped matrix: " + str(matrix.reshape(2,6)))