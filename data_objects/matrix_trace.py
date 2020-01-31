# Problem: you need to calculate the trace of a matrix.
# i.e. - the sum of diagonal elements

import numpy as np

# create a matrix
matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# return the trace
print("Matrix trace: ")
print(matrix.trace())