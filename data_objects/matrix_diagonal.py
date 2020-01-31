# Problem: you need to get the diagonal elements of a matrix

import numpy as np

matrix = np.array([
    [1,2,3],
    [2,4,6],
    [3,8,9]
])

# return diagonal elements
print("Diagonal elements: ")
print(matrix.diagonal())