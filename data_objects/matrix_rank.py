# Problem: You need to find the rank of a matrix
# i.e.  - the rank of a matrix is the dimensions of the vector space spanned by it's columns or rows.

import numpy as np

# create matrix
matrix = np.array([
    [1,2,1],
    [2,2,2],
    [2,3,3]
])

# return matrix rank
print("Matrix rank: " + str(np.linalg.matrix_rank(matrix)))

# create matrix
matrix = np.array([
    [1,1,1,3],
    [1,1,10,2],
    [1,1,15,5]
])

# return matrix rank
print("Matrix rank: " + str(np.linalg.matrix_rank(matrix)))