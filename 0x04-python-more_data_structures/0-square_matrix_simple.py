#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for j in range(len(matrix)):
        temp = []
        for i in range(len(matrix[j])):
            temp += matrix[j][i]**2
        result += temp
    print(result)
