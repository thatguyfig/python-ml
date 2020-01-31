# matrices are similar to vectors, however they have another dimension. 
# AKA: Tables
# problem: Create a Matrix
import numpy as np

# create a normal matrix
def create_matrix():
    matrix_object = np.array([
        [1,2], 
        [1,3],
        [1,4]
    ])

    return matrix_object


matrix = create_matrix()
print("Matrix:")
print(matrix)


# create a sparse matrix
from scipy import sparse

def create_matrix_sparse():

    # create a normal matrix
    matrix_object = np.array([
        [1,2], 
        [1,3],
        [1,4]
    ])

    # create a compressed row matrix
    matrix_sparse = sparse.csr_matrix(matrix_object)
    return matrix_sparse

sparse_matrix = create_matrix_sparse()

print("Sparse Matrix:" + str(sparse_matrix))

# describe the matrix
print("Matrix shape: " + str(matrix.shape))
print("Matrix size: " + str(matrix.size))
print("Matrix dimenions: " + str(matrix.ndim))