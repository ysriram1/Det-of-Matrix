# Author: Sriram Yarlagadda
# (uses recursion)
import numpy as np

def subset_matrix(M, i, j):
    '''
    returns a matrix (numpy array) after removing row i and col j
    '''
    M = np.delete(M, i, 0)
    M = np.delete(M, j, 1)

    return M


def det(M):
    '''
    returns the determinant of matrix M
    Inputs
        M: array-like (nested-list is fine) square matrix
    '''
    M = np.array(M)
    rows, cols = M.shape

    assert rows == cols, 'Must be a square matrix'

    # base-case (if 2x2 matrix)
    if rows == 2:
        return M[0][0]*M[1][1] - M[0][1]*M[1][0]

    # recursive case
    if rows > 2:
        return sum(-M[0,j] * det(subset_matrix(M, 0, j))\
                   if j%2 == 1 \
                   else M[0,j] * det(subset_matrix(M, 0, j)) \
                   for j in range(cols) )
