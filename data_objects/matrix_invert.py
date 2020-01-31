# Problem: you want to calculate the inverse of a square matrix

import numpy as np

# create a matrix
matrix = np.array([
    [1,4],
    [2,5]
])

print("Normal Matrix: \n%s"  % matrix)

# calculate the inverse of it
print("Inverse Matrix: \n%s" % np.linalg.inv(matrix))

# multiple the orginal matrix by the inverse to get the identity matrix
print("Identity Matrix: \n%s" % (matrix @ np.linalg.inv(matrix)))