import numpy as np

mat1 = []
mat2 = []
mat3 = []
k = int(input())
if k == 1:
    m = int(input("Введите количество столбцов -"))
    n = int(input("Введите количество строк -"))

    if m != n:
        print("Вычисление определителя возможно только для квадратной матрицы")

    if m == n == 2:
        print("Введите матрицу -")
        for i in range(m):
            a = []
            for j in range(n):
                a.append(int(input()))
            mat1.append(a)

        r = mat1[0][0] * mat1[1][1] - mat1[0][1] * mat1[1][0]
        print("Результат -", r)

    if m == n == 3:
        print("Введите матрицу -")
        for i in range(m):
            a = []
            for j in range(n):
                a.append(int(input()))
            mat1.append(a)
        r1 = (mat1[0][0] * mat1[1][1] * mat1[2][2] + mat1[0][1]*mat1[1][2] * mat1[2][0] + mat1[1][0]*mat1[2][1] * mat1[0][2])
        r2 = (mat1[0][2] * mat1[1][1] * mat1[2][0] + mat1[0][1]*mat1[1][0] * mat1[2][2] + mat1[0][0]*mat1[1][2] * mat1[2][1])
        print("Определитель = ", r1 - r2)

    if m == n == 4:
            print("Введите матрицу -")
            for i in range(m):
                a = []
                for j in range(n):
                    a.append(int(input()))
                mat1.append(a)
            r1 = (mat1[1][1] * mat1[2][2] * mat1[3][3] + mat1[1][2] * mat1[2][3] * mat1[3][1] + mat1[2][1] * mat1[3][2] * mat1[1][3]) - (mat1[1][3] * mat1[2][2] * mat1[3][1] + mat1[1][2]*mat1[2][1] * mat1[3][3] + mat1[1][1]*mat1[2][3] * mat1[3][2])
            r2 = (mat1[1][0] * mat1[2][2] * mat1[3][3] + mat1[1][2] * mat1[2][3] * mat1[3][0] + mat1[1][3] * mat1[2][0] * mat1[3][2]) - (mat1[1][3] * mat1[2][2] * mat1[3][0] + mat1[3][2]*mat1[2][3] * mat1[1][0] + mat1[2][0]*mat1[1][2] * mat1[3][3])
            r3 = (mat1[1][0] * mat1[2][1] * mat1[3][3] + mat1[2][0] * mat1[3][1] * mat1[1][3] + mat1[1][1] * mat1[2][3] * mat1[3][0]) - (mat1[1][3] * mat1[2][1] * mat1[3][0] + mat1[2][0]*mat1[1][1] * mat1[3][3] + mat1[3][1]*mat1[2][3] * mat1[1][0])
            r4 = (mat1[1][0] * mat1[2][1] * mat1[3][2] + mat1[2][0] * mat1[3][1] * mat1[1][2] + mat1[1][1] * mat1[2][2] * mat1[3][0]) - (mat1[1][2] * mat1[2][1] * mat1[3][0] + mat1[3][1] * mat1[2][2] * mat1[1][0] + mat1[2][0] * mat1[1][1] * mat1[3][2])
            r = mat1[0][0] * r1 - mat1[0][1] * r2 + mat1[0][2] * r3 - mat1[0][3] * r4
            print("Определитель = ", r)

    if m == n == 5:
        print("Введите матрицу -")
        for i in range(m):
            a = []
            for j in range(n):
                a.append(int(input()))
            mat1.append(a)
        r = np.linalg.det(mat1)
        print("Результат = ", f"{r:.0f}")

    if m == n == 6:
        print("Введите матрицу -")
        for i in range(m):
            a = []
            for j in range(n):
                a.append(int(input()))
            mat1.append(a)
        r = np.linalg.det(mat1)
        print("Результат = ", f"{r:.0f}")

    if m == n == 7:
        print("Введите матрицу -")
        for i in range(m):
            a = []
            for j in range(n):
                a.append(int(input()))
            mat1.append(a)
        r = np.linalg.det(mat1)
        print("Результат = ", f"{r:.0f}")

