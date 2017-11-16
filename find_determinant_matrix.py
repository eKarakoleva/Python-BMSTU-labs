import math as m

n = int(input('Number of rows and col: '))
mat = []

sign = 1

for i in range(n):
    a = list(map(float, input('Row numbers: ').split()))
    mat.append(a)

for j in range(n):
    maxI = 0
    maxV = -1
    for i in range(j, n):
        if maxV < abs(mat[i][j]):
            maxV = abs(mat[i][j])
            maxI = i

    for i in range(maxI, j, -1):
        mat[i], mat[i - 1] = mat[i - 1], mat[i]
        sign *= -1

    for i in range(j + 1, n):
        if mat[i][j] == 0:
            continue
        m_number = mat[i][j] / mat[j][j]
        a1 = [x * m_number for x in mat[j]]
        sub = [a - b for a, b in zip(mat[i], a1)]
        mat[i] = sub

deter = 1
for i in range(n):
    deter *= mat[i][i]

print('Determinant = %f' % (deter * sign))
