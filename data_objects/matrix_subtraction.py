# Problem: You need to add two matrices together

import numpy as np

# create matrix
matrix_a = np.array([
    [1,1,1],
    [1,1,1],
    [1,1,2]
])

matrix_b = np.array([
    [1,3,1],
    [1,3,1],
    [1,3,8]
])

# sub two matrices
print("Matrix subtraction: " + str(np.subtract(matrix_a, matrix_b)))

# we can also use simple operators
print("Matrix subtraction (simple): " + str(matrix_a - matrix_b))