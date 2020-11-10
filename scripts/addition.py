# Matrices have a wide range of applications in programming: they're used for digital image processing, 
# graph representation and algorithms on a graph, graphic effects, applied math, statistics, and much more.
# Since matrices are tables of numbers, they are usually presented in code as 2D-arrays. 
# In this project, you will learn how to read and output matrices, do operations on them, 
# and compute the determinant of a square matrix. At first, you will work with matrices with integer elements, 
# and later the elements will be floating-point numbers.
#
# Description
# Let’s start with matrix addition.
# For two matrices to be added, they must have an equal number of rows and columns. 
# The sum of matrices AA and BB will be a matrix with the same number of rows and columns as AA or BB. 
# The sum of AA and BB, denoted A + BA+B or B + AB+A, is computed by adding the corresponding elements of AA and BB.
#
# Objectives
# In this stage, you should write a program that:
# - reads matrix AA from the input.
# - reads matrix BB from the input.
# - outputs their sum if it is possible to add them; otherwise, it should output the ERROR message.
# Each matrix in the input is given in the following way: the first line contains the number of rows nn and the number of columns mm. 
# Then nn lines follow, each containing mm integers representing one row of the matrix.
# Output the result in the same way but don't print the dimensions of the matrix.
#
# Examples
# Example 1:
# Input:
# 4 5
# 1 2 3 4 5
# 3 2 3 2 1
# 8 0 9 9 1
# 1 3 4 5 6
# 4 5
# 1 1 4 4 5
# 4 4 5 7 8
# 1 2 3 9 8
# 1 0 0 0 1
# Output:
# 2 3 7 8 10
# 7 6 8 9 9
# 9 2 12 18 9
# 2 3 4 5 7
# 
# Example 2:
# Input:
# 2 3
# 1 4 5
# 4 5 5
# 4 5
# 0 1 0 4 5
# 1 7 8 9 4
# 1 2 3 5 6
# 1 3 4 3 8
# Output:
# ERROR

class Matrix:
    """Create a numeric matrix.
    
    Arguments:
        row_dim -- The number of matrix rows
        col_dim -- The number of matrix columns

    Keyword arguments:
        rows -- The matrix rows (if not passed, they will be read from input)
    """
    def __init__(self, row_dim, col_dim, rows=None):
        self.row_dim = row_dim
        self.col_dim = col_dim
        self.rows = []

        if not rows:
            self.get_rows()
        else:
            self.rows = rows
        
    def get_rows(self):
        """Get the matrix rows from input."""
        index = 0

        while index < self.row_dim:
            self.rows.append(list(map(int,input().split())))
            index = index + 1

    def repr(self, repr_type=None):
        """Print a representation of the matrix.
        
        Keyword arguments:
            repr_type -- The matrix representation type; 
                         if None is passed then the matrix will be printed as an array of arrays
        """
        if not repr_type:
            print(self.rows)
        else:
            for i in range(0, self.row_dim):
                print(' '.join([str(x) for x in self.rows[i]]))


def mat_addition(a, b):
    """Add two matrices.

    Arguments:
        a -- The first matrix
        b -- The second matrix

    Returns:
        A matrix if the addition could be performed, or None
    """
    if a.row_dim != b.row_dim or a.col_dim != b.col_dim:
        return None
    rows = []
    for i in range(0, a.row_dim):
        cols = []
        for j in range(0, a.col_dim):
            cols.append(a.rows[i][j] + b.rows[i][j])
        rows.append(cols)
    return Matrix(a.row_dim, a.col_dim, rows)

x, y = map(int,input().split())
mat_A = Matrix(x, y)
x, y = map(int,input().split())
mat_B = Matrix(x, y)
mat_C = mat_addition(mat_A, mat_B)

if mat_C:
    mat_C.repr("table")
else:
    print("ERROR")