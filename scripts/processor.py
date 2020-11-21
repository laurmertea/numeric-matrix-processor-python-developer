import sys


# MENU SETUP
menu_options = ['1. Add matrices', '2. Multiply matrix by a constant', '3. Multiply matrices', '0. Exit']
selected_option = None


# MESSAGES SETUP
impossible_operation = "The operation cannot be performed.\n"
matrix_size_input = "Enter size of matrix: "
first_matrix_size_input = "Enter size of first matrix: "
second_matrix_size_input = "Enter size of second matrix: "
matrix_input = "Enter matrix:"
first_matrix_input = "Enter first matrix:"
second_matrix_input = "Enter second matrix:"
constant_input = "Enter constant: "
result_output = "The result is:"
unsupported_option = "Not supported!"


def exit_proc(message=""):
    """Exit with optional message.
    
    Keyword arguments:
        message -- string to exit with as message (default is an empty string)
    """
    sys.exit(message)


def processor_menu(selected):
    """Try and access selected option in the processor menu (see the `menu_options` list).

    Arguments:
        selected -- a valid integer matching an option from menu_options list
    """
    if selected_option == 0:
        exit_proc()
    else:
        if selected_option == 1:
            x, y = map(int,input(first_matrix_size_input).split())
            print(first_matrix_input)
            mat_A = Matrix(x, y)
            x, y = map(int,input(second_matrix_size_input).split())
            print(second_matrix_input)
            mat_B = Matrix(x, y)

            mat_C = mat_addition(mat_A, mat_B)
            if mat_C:
                print(result_output)
                mat_C.repr("table")
            else:
                print(impossible_operation)            
        elif selected_option == 2:
            x, y = map(int,input(matrix_size_input).split())
            print(matrix_input)
            mat_A = Matrix(x, y)
            multiplier = float(input(constant_input))
            mat_B = mat_multiply_constant(mat_A, multiplier)
            if mat_B:
                print(result_output)
                mat_B.repr("table")
            else:
               print(impossible_operation) 
        elif selected_option == 3:
            x, y = map(int,input(first_matrix_size_input).split())
            print(first_matrix_input)
            mat_A = Matrix(x, y)
            x, y = map(int,input(second_matrix_size_input).split())
            print(second_matrix_input)
            mat_B = Matrix(x, y)

            mat_C = mat_multiply(mat_A, mat_B)
            if mat_C:
                print(result_output)
                mat_C.repr("table")
            else:
                print(impossible_operation)   
        else:
            print(unsupported_option)


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
            self.rows.append(list(map(float,input().split())))
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


def mat_transpose(mat):
    """Transpose a matrix.

    Arguments:
        mat -- The matrix

    Returns:
        A matrix
    """
    rows = []
    for j in range(0, mat.col_dim):
        cols = []
        for i in range(0, mat.row_dim):
            cols.append(mat.rows[i][j])
        rows.append(cols)
    return Matrix(mat.col_dim, mat.row_dim, rows)


def mat_multiply(mat_a, mat_b):
    """Multiply two matrices.

    Arguments:
        mat_a -- The first matrix
        mat_b -- The second matrix

    Returns:
        A matrix if the multiplication could be performed, or None
    """
    if mat_a.col_dim != mat_b.row_dim:
        return None
    
    mat_bt = mat_transpose(mat_b)
    rows = []
    for i in range(0, mat_a.row_dim):
        cols = []
        for j in range(0, mat_bt.row_dim):
            result = 0
            for k in range(0, mat_a.col_dim):
                result += mat_a.rows[i][k] * mat_bt.rows[j][k]
            cols.append(result)
        rows.append(cols)
    return Matrix(mat_a.row_dim, mat_b.col_dim, rows)


while selected_option not in range(0, 3):
    while selected_option != 0:
        selected_option = int(input('\n'.join(menu_options) + '\n' + 'Your choice: '))
        processor_menu(selected_option)
