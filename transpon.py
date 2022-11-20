import numpy as np

m = int(input("Введите количество столбцов -"))
n = int(input("Введите количество строк -"))
mat1 = []
mat2 = [[0]] * n * n

print("Введите матрицу -")
for i in range(n):
    a = []
    for j in range(m):
        a.append(int(input()))
    mat1.append(a)
if m == n:
    mat2 = np.transpose(mat1)

print("Трансопнированная - ", mat2)
