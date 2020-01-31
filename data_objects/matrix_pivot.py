# Problem: Transpose a vector or matrix - i,e. pivot it

# library
import numpy as np

# create matrix
matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# normal matrix
print("Normal matix: " + str(matrix))

# transpose matrix
print("Transposed matrix: " + str(matrix.T))

