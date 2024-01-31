def print_upper_triangle(matrix: [[]]) -> None:
    """
    Prints the upper triangle of a matrix
    :param matrix: a matrix in size n * n which contains chars
    :return: None
    """
    PRINTED_COLUMN_SIZE = 5  # num of chars in column
    if not isinstance(matrix, list):
        raise TypeError('Expected matrix to be a list')

    number_of_rows = len(matrix)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError('One or more of the elements in given list is not a list.')
        if len(row) != number_of_rows:
            raise ValueError('Expected number of rows and columns in matrix to be the same')

    for row_index, row in enumerate(matrix):
        print((' ' * PRINTED_COLUMN_SIZE) * row_index, end='')
        for column_index in range(row_index, len(row)):
            spaces_at_end = PRINTED_COLUMN_SIZE - len(str(row[column_index]))
            print(row[column_index], end=(' ' * spaces_at_end))
        print()
