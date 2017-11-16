import math as m

n = int(input('Number of rows and col of matrixes: '))
mat1 = []
mat2 = []

for i in range(n):
    a = list(map(float, input('Row numbers: ').split()))
    mat1.append(a)

print()

for i in range(n):
    a = list(map(float, input('Row numbers: ').split()))
    mat2.append(a)

res = 0
mat_res = []

for j in range(n):
    seen = []
    for f in range(n):
        res=0
        for k in range(n):
            res += mat1[j][k] * mat2[k][f]
        seen.append(res)
    mat_res.append(seen)
    
print()

for row in mat_res:
    print(row)

 
