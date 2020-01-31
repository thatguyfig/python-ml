# Find the minimum or maximum values in a matrix / array
import numpy as np

# create matrix
matrix  = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# return maximum element
print("Max element value: " + str(np.max(matrix)))

# return minimum element
print("Min element value: " + str(np.min(matrix)))