# Problem: You need to know the determinant of a matrix
# i.e. - 

import numpy as np

# create matrix
matrix = np.array([
    [10,20],
    [4,5]
])

# get the determinant of the matrix
print("Matrix determinant: " + str(np.linalg.det(matrix)))