#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    final = []
    for j in range(len(matrix)):
        result = map(lambda x: x*x, matrix[j])
        final.append(list(result))
    return final
