def square_matrix_simple(matrix=[]):
    return [[element * element for element in row] for row in matrix]
   # return list(map(lambda x: x * x, row) for row in matrix)
