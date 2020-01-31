# Problem: You need to multiply two matrices together

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

# multiple two matrices using the dot product
print("Multipy through dot: " + str(np.dot(matrix_a, matrix_b)))

# multiply using @ operator to declare
print("Multipy through @ operator: " + str(matrix_a @ matrix_b))

# we can also do element-wise multiplication, which is more straight forward
print("Multiple element-wise: " + str(matrix_a * matrix_b))