## vectors are considered 3 integer groups which can denote 3d space.
## AKA: one-dimensional arrays
## problem : you need to create a vector
## solution:

import numpy as np

def create_vector_row(x, y, z):
    vector_row = np.array([x,y,z])
    return vector_row

def create_vector_column(x, y, z):
    vector_column = np.array([
        [x],
        [y],
        [z]
    ])
    return vector_column

vec_row = create_vector_row(1,2,3)
vec_column = create_vector_column(1,2,3)

print("Vector row:")
print(vec_row)

print("Vector col:")
print(vec_column)