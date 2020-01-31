# Problem: You need to fid the eigenvalues and eigenvectors of a square matrix
## 
## What are these?
##
## Eigenvectors are widely used in machine learning libraries. 
## Intuitively, given a linear transformation represented by a matrix, A, eigenvectors are vectors that, when the transformation is applied,
## change only in scale (not direction).
##


import numpy as np

# create the matrix
matrix = np.array([
    [1, -1, 3],
    [1, 1, 6],
    [3, 8, 9]
])

# calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# log them out
print("Eigenvalues: " + str(eigenvalues))
print("Eigenvectors: " + str(eigenvectors))