# Here we will look at how to access invidivual elements of the array / matrix
import numpy as np

## VECTORS
# create a vector
vector = np.array([1,2,3,4,5,6])
# select the third element of the vector
print("Vector element 3: " + str(vector[2]))

## MATRICES
# create a matrix
matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
# print the 2nd value in the 3rd row
print("Matrix element [2] [1]: "+ str(matrix[2][1]))


## SLICING VECTORS
# select all elements of a vector
print("All elements: " + str(vector[:]))

# select everything up to and including third element
print("Up to third element: " + str(vector[:3]))

# select everything after the third element
print("After the third element: " + str(vector[3:]))

# select the last element
print("Last element: " + str(vector[-1])

## SLICING MATRICES
# select the first two rows and all columns of a matrix
print("First two rows and all columns (matrix): " + str(matrix[:2,:]))

# select all rows and the second column
print("All rows and second column (matrix): " + str(matrix[:,1:2]))

