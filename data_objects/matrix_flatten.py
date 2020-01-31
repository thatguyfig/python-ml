# Problem: you need to transform a matrix into a one-dimensional array

import numpy as np

# create matrix
matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# flatten matrix
print(matrix.flatten())