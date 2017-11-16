import math as m

n = int(input('Enter number of rows (NxN)'))
matrix = []
for i in range(n):
    row = list(map(int,input('Enter row:').split()))
    matrix.append(row)

diag1 = 0
diag2 = 0
for i in range(n):
    k = len(matrix[i]) - 1 - i
    diag2 = matrix[i][k]
    for j in range(len(matrix[i])):
        if i == j:
            diag1 = matrix[i][j]
            matrix[i][j] = diag2
            matrix[i][k] = diag1

for row in matrix:
    print(row)