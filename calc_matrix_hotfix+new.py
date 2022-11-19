
print("Что Вы хотите сделать - ")
k = int(input("1. Сложить две матрицы\n2. Умножить матрицу 1 на матрицу 2\n3. Вычесть из 1 матрицы 2 матрицу\n4. Умножение матрицы на коснтанту\nВаш выбор - "))

mat1 = []
mat2 = []
mat3 = []
if k == 1:
    m = int(input("Введите количество столбцов -"))
    n = int(input("Введите количество строк -"))

    print("Введите первую матрицу -")
    for i in range(m):
        a = []
        for j in range(n):
            a.append(int(input()))
        mat1.append(a)

    print("Введите вторую матрицу -")
    for i in range(m):
        b = []
        for j in range(n):
            b.append(int(input()))
        mat2.append(b)

    for i in range(m):
        c = []
        for j in range(n):
            if m == n:
                c.append(mat1[i][j] + mat2[i][j])
        mat3.append(c)

    print("Матрица суммы - ")
    for i in range(m):
        for j in range(n):
            print(mat3[i][j], end=" ")
        print()

if k == 2:
    m = int(input("Введите количество столбцов -"))
    n = int(input("Введите количество строк -"))
    print("Введите первую матрицу -")
    for i in range(m):
        a = []
        for j in range(n):
            a.append(int(input()))
        mat1.append(a)

    print("Введите вторую матрицу -")
    for i in range(m):
        b = []
        for j in range(n):
            b.append(int(input()))
        mat2.append(b)
    mat3 = [[sum(a * b for a, b in zip(m, n)) for n in zip(*mat2)] for m in mat1]
    # mxn m1xn1 = mxn1

    print("Произведение матриц = ")
    for i in range(m):
        for j in range(n):
            print(mat3[i][j], end=" ")
        print()

if k == 3:
    m = int(input("Введите количество столбцов -"))
    n = int(input("Введите количество строк -"))

    print("Введите первую матрицу -")
    for i in range(m):
        a = []
        for j in range(n):
            a.append(int(input()))
        mat1.append(a)

    print("Введите вторую матрицу -")
    for i in range(m):
        b = []
        for j in range(n):
            b.append(int(input()))
        mat2.append(b)

    for i in range(m):
        c = []
        for j in range(n):
            if m == n:
                c.append(mat1[i][j] - mat2[i][j])
        mat3.append(c)

    print("Матрица разности - ")
    for i in range(m):
        for j in range(n):
            print(mat3[i][j], end=" ")
        print()
if k == 4:
    m = int(input("Введите количество столбцов -"))
    n = int(input("Введите количество строк -"))
    k = int(input("Введите число - "))

    print("Введите матрицу -")
    for i in range(m):
        a = []
        for j in range(n):
            a.append(int(input()))
        mat1.append(a)

    for i in range(m):
        c = []
        for j in range(n):
            c.append(k * mat1[i][j])
        mat3.append(c)

    print("Результат - ")
    for i in range(m):
        for j in range(n):
            print(mat3[i][j], end=" ")
        print()