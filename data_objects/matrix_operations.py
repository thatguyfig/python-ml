# Problem: You want to apply some function to multiple elements in an array.

# load library
import numpy as np

# create a matrix
matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# create function that adds 100 to something
add_100 = lambda t: t + 100

# create vectorised function
vectorised_add_100 = np.vectorize(add_100)

# Apply function to all elements in the matrix
print(vectorised_add_100(matrix))
