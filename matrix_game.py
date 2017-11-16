import math as m
import numpy as np

matrix = []
n = int(input('Number of rows and col of matrixes: '))
print()
for i in range(n):
    a = list(input('Row numbers: ').split())
    matrix.append(a)

new_matrix = np.copy(matrix)
for i in range(n):
    for j in range(len(matrix[i])):
        if matrix[i][j].isnumeric():
            for q in range(len(matrix[i])):
                new_matrix[i][q] = matrix[i][j]
                new_matrix[q][j] = matrix[i][j]
print(new_matrix)

