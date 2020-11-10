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


def mat_addition(mat_a, mat_b):
    """Add two matrices.

    Arguments:
        mat_a -- The first matrix
        mat_b -- The second matrix

    Returns:
        A matrix if the addition could be performed, or None
    """
    if mat_a.row_dim != mat_b.row_dim or mat_a.col_dim != mat_b.col_dim:
        return None
    rows = []
    for i in range(0, mat_a.row_dim):
        cols = []
        for j in range(0, mat_a.col_dim):
            cols.append(mat_a.rows[i][j] + mat_b.rows[i][j])
        rows.append(cols)
    return Matrix(mat_a.row_dim, mat_a.col_dim, rows)


def mat_multiply_constant(mat, const):
    """Multiply a matrix by a constant value.

    Arguments:
        mat -- The matrix
        const -- The constant

    Returns:
        A matrix
    """
    rows = []
    for i in range(0, mat.row_dim):
        cols = []
        for j in range(0, mat.col_dim):
            cols.append(mat.rows[i][j] * const)
        rows.append(cols)
    return Matrix(mat.row_dim, mat.col_dim, rows)


x, y = map(int,input().split())
mat_A = Matrix(x, y)
x, y = map(int,input().split())
mat_B = Matrix(x, y)

mat_C = mat_addition(mat_A, mat_B)
if mat_C:
    mat_C.repr("table")
else:
    print("ERROR")

x, y = map(int,input().split())
mat_D = Matrix(x, y)
multiplier = int(input())
mat_E = mat_multiply_constant(mat_D, multiplier)
mat_E.repr("table")
