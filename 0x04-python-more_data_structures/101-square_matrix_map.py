#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    def help_function(row): return list(map(lambda: element, element ** 2))
    return list(map(lambda row: list(
        map(lambda element: element ** 2, row)), matrix))
