def luDecomposition(mat, n):
    lower = [[0 for x in range(n)]
             for y in range(n)]
    upper = [[0 for x in range(n)]
             for y in range(n)]
    for i in range(n):
        for k in range(i, n):
            soma = 0
            for j in range(i):
                soma += (lower[i][j] * upper[j][k])
            upper[i][k] = mat[i][k] - soma

        for k in range(i, n):
            if (i == k):
                lower[i][i] = 1
            else:
                soma = 0
                for j in range(i):
                    soma += (lower[k][j] * upper[j][i])
                if (upper[i][i] != 0):
                    lower[k][i] = (mat[k][i] - soma) / (upper[i][i])

    print("L matrix - \n")
    for i in range(n):
        # Lower
        for j in range(n):
            print(float(round(lower[i][j], 1)), end="  ")
        print("", end="\n")
    print("U matrix - \n")
    for i in range(n):
        for j in range(n):
            print(float(round(upper[i][j], 1)), end="  ")
        print("", end="\n")

def transpone(a):
    zip_row = zip(*a)
    b = [list(row) for row in zip_row]
    return b

def determinant(A, total=0):
    indices = list(range(len(A)))
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val

    for fc in indices:
        As = A
        As = As[1:]
        height = len(As)
        for i in range(height):
            As[i] = As[i][0:fc] + As[i][fc + 1:]
        sign = (-1) ** (fc % 2)
        sub_det = determinant(As)
        total += sign * A[0][fc] * sub_det
    return total

def ln(x):
    if x > 0:
        value = 10 ** 8 * ((x ** (1 / 10 ** 8)) - 1)
        return value
    else:
        return None


def log(x, base):
    if x > 0 and base > 0:
        value = ln(x) / ln(base)
        return value
    else:
        return None


def factorial(x):
    for i in range(1, x):
        x *= i
    return x


def sin(x):
    x *= 3.1415926 / 180
    value = x
    sign = -1
    for i in range(3, 100, 2):
        value += (x ** i / factorial(i) * sign)
        sign *= -1
    return round(value, 4)


def cos(x):
    x *= 3.1415926 / 180
    value = 1
    sign = -1
    for i in range(2, 100, 2):
        value += (x ** i / factorial(i) * sign)
        sign *= -1
    return round(value, 4)


def tg(x):
    if not cos(x) == 0:
        return round(sin(x) / cos(x), 4)
    else:
        return None


def ctg(x):
    if not sin(x) == 0:
        return round(cos(x) / sin(x), 4)
    else:
        return None



def arcsin(x):
    if -1 < x < 1:
        x = x + x**3/6 + 3*x**5/40 + 5*x**7/112 + 35*x**9/1152 + 81*x**11/2816 + 231*x**13/13312 + 429*x**15/30720
        return x
    elif x == 1 or x == -1:
        return x * 1.57079632679
    else:
        return None

def arccos(x):
    if -1 <= x < 1:
        x = 3.141592653589793238/2 - arcsin(x)
        return x
    elif x == 1:
        return 0
    else:
        return None


def arctg(x):
    x = arcsin(x / ((1 + x ** 2) ** 0.5))
    return x


def arcctg(x):
    x = arccos(x / ((1 + x ** 2) ** 0.5))
    return x


k = int(input(
    "В каком модуле хотите выполнять вычисления:\n1. Простые вычисление.\n2. Тригонометрия.\n3. Матрицы.\nВаш выбор - "))
print("---------------\n")
if k == 1:
    print("---------------\n")
    c = int(
        input("Что хотите сделать:\n1. Сложение.\n2. Вычитание.\n3. Умножение.\n4. Деление.\n5. Возведение в степень."
              "\n6. Извлечение из под корня.\n7. Вычислить натуральный логарифм.\n8. Логарифм.\nВаш выбор -  "))
    if c == 1:
        a = int(input("Введите первое число - "))
        b = int(input("Введите второе число - "))
        print("---------------\n")
        print("Результат - ", a + b)
    if c == 2:
        a = int(input("Введите первое число - "))
        b = int(input("Введите второе число - "))
        print("---------------\n")
        print("Результат - ", a - b)
    if c == 3:
        a = int(input("Введите первое число - "))
        b = int(input("Введите второе число - "))
        print("---------------\n")
        print("Результат - ", a * b)
    if c == 4:
        a = int(input("Введите первое число - "))
        b = int(input("Введите второе число - "))
        print("---------------\n")
        print("Результат - ", a / b)
    if c == 5:
        a = int(input("Введите число - "))
        b = int(input("Введите степень - "))
        print("---------------\n")
        print("Результат - ", a ** b)
    if c == 6:
        a = int(input("Введите первое число - "))
        b = int(input("Введите степень корня - "))
        print("---------------\n")
        print("Результат - ", (a) ** (1 / b))
    if c == 7:
        a = int(input("Введите число - "))
        print("---------------\n")
        print("Результат - ", ln(a))
    if c == 8:
        a = int(input("Введите основание логарифма - "))
        b = int(input("Введите число логарифма - "))
        print("---------------\n")
        print("Результат - ", f"{log(b, a):.3f}")

if k == 2:
    k = int(input("Что хотим посчитать:\n1. Синус (sin).\n2. Косинус (cos).\n3. Тангенс (tg).\n4. Котангенс (ctg)."
                  "\n5. Арксинус (arcsin).\n6. Арккосинус (arccos).\n7. Арктангенс (arctg).\n8. Арккотангенс (arcctg).\nВаш выбор - "))
    print("---------------\n")
    if k == 1:
        x = float(input("Введите угол в градусах - "))
        print("---------------\n")
        print("Результат - ", sin(x))
    if k == 2:
        x = float(input("Введите угол в градусах - "))
        print("---------------\n")
        print("Результат - ", cos(x))
    if k == 3:
        x = float(input("Введите угол в градусах - "))
        print("---------------\n")
        print("Результат - ", tg(x))
    if k == 4:
        x = float(input("Введите угол в градусах - "))
        print("---------------\n")
        print("Результат - ", ctg(x))
    if k == 5:
        x = float(input("Введите угол в градусах - "))
        print("---------------\n")
        print("Результат - ", arcsin(x))
    if k == 6:
        x = float(input("Введите угол в градусах - "))
        print("---------------\n")
        print("Результат - ", arccos(x))
    if k == 7:
        x = float(input("Введите угол в градусах - "))
        print("---------------\n")
        print("Результат - ", arctg(x))
    if k == 8:
        x = float(input("Введите угол в градусах - "))
        print("---------------\n")
        print("Результат - ", arcctg(x))

if k == 3:
    print("Что Вы хотите сделать - ")
    k = int(input("1. Сложить две матрицы.\n2. Вычесть из 1 матрицы 2 матрицу.\n3. Умножить матрицу 1 на матрицу 2."
                  "\n4. Умножение матрицы на константу.\n5. Транспонирование матрицы.\n6. Найти определитель.\n7. Написать LU разложение.\nВаш выбор - "))
    print("---------------\n")
    mat1 = []
    mat2 = []
    mat3 = []
    #сложение
    if k == 1:
        m = int(input("Введите количество столбцов -"))
        n = int(input("Введите количество строк -"))
        if m == n:
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
                    print("---------------\n")
                    print(mat3[i][j], end=" ")
                print()
    #вычитание
    if k == 2:
        m = int(input("Введите количество столбцов -"))
        n = int(input("Введите количество строк -"))
        m1 = int(input("Введите количество столбцов -"))
        n1 = int(input("Введите количество строк -"))

        if m != m1 and n != n1:
            print("Вычитание матриц возможно только для матриц одинаковых размеров")

        if m == n:

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

            for i in range(m):
                for j in range(n):
                    print("---------------\n")
                    print("Результат - ", mat3[i][j], end=' ')
                print()
    #произведение
    if k == 3:
        m = int(input("Введите количество столбцов 1 матрицы -"))
        n = int(input("Введите количество строк 1 матрицы -"))
        m1 = int(input("Введите количество столбцов 2 матрицы -"))
        n1 = int(input("Введите количество строк 2 матрицы -"))

        if n != m1:
            print(
                "Для проивзедения матриц нужно, чтобы количество строк 1 матрицы было равно количеству столбцов 2 матрицы")

        if n == m1:

            print("Введите первую матрицу -")
            for i in range(m):
                a = []
                for j in range(n):
                    a.append(int(input()))
                mat1.append(a)

            print("Введите вторую матрицу -")
            for i in range(m1):
                b = []
                for j in range(n1):
                    b.append(int(input()))
                mat2.append(b)
            if n != m:
                print("Произведение матриц возможно при одинаковом количесте столбцов первой матрицы и строк второй матрицы")
            mat3 = [[0 for m in range(m)] for n1 in range(n1)]
            for i in range(m):
                for j in range(n1):
                    for k in range(n):
                        mat3[i][j] += mat1[i][k] * mat2[k][j]
            print("---------------\n")
            for i in range(m):
                for j in range(n1):
                    print(mat3[i][j], end=' ')
                print()
    #умножение на константу
    if k == 4:
        m = int(input("Введите количество столбцов -"))
        n = int(input("Введите количество строк -"))
        k = int(input("Введите константу - "))
        if m == n:
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
            print("---------------\n")
            print("Результат = ")
            for i in range(m):
                for j in range(n):
                    print(mat3[i][j], end=" ")
                print()
    #транспонирование
    if k == 5:
        m = int(input("Введите количество столбцов -"))
        n = int(input("Введите количество строк -"))
        print("Введите матрицу -")
        for i in range(m):
            a = []
            for j in range(n):
                a.append(int(input()))
            mat1.append(a)
        print("---------------\n")
        print("Транспонированная - \n")
        mat2 = transpone(mat1)
        for i in range(n):
            for j in range(m):
                print(mat2[i][j], end=' ')
            print()

    #определитель
    if k == 6:
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
            print("---------------\n")
            print("Результат -", r)

        if m == n == 3:
            print("Введите матрицу -")
            for i in range(m):
                a = []
                for j in range(n):
                    a.append(int(input()))
                mat1.append(a)
            r1 = (mat1[0][0] * mat1[1][1] * mat1[2][2] + mat1[0][1] * mat1[1][2] * mat1[2][0] + mat1[1][0] * mat1[2][
                1] *
                  mat1[0][2])
            r2 = (mat1[0][2] * mat1[1][1] * mat1[2][0] + mat1[0][1] * mat1[1][0] * mat1[2][2] + mat1[0][0] * mat1[1][
                2] *
                  mat1[2][1])
            print("---------------\n")
            print("Определитель = ", r1 - r2)

        if m == n == 4:
            print("Введите матрицу -")
            for i in range(m):
                a = []
                for j in range(n):
                    a.append(int(input()))
                mat1.append(a)
            r1 = (mat1[1][1] * mat1[2][2] * mat1[3][3] + mat1[1][2] * mat1[2][3] * mat1[3][1] + mat1[2][1] * mat1[3][
                2] *
                  mat1[1][3]) - (
                             mat1[1][3] * mat1[2][2] * mat1[3][1] + mat1[1][2] * mat1[2][1] * mat1[3][3] + mat1[1][1] *
                             mat1[2][3] * mat1[3][2])
            r2 = (mat1[1][0] * mat1[2][2] * mat1[3][3] + mat1[1][2] * mat1[2][3] * mat1[3][0] + mat1[1][3] * mat1[2][
                0] *
                  mat1[3][2]) - (
                             mat1[1][3] * mat1[2][2] * mat1[3][0] + mat1[3][2] * mat1[2][3] * mat1[1][0] + mat1[2][0] *
                             mat1[1][2] * mat1[3][3])
            r3 = (mat1[1][0] * mat1[2][1] * mat1[3][3] + mat1[2][0] * mat1[3][1] * mat1[1][3] + mat1[1][1] * mat1[2][
                3] *
                  mat1[3][0]) - (
                             mat1[1][3] * mat1[2][1] * mat1[3][0] + mat1[2][0] * mat1[1][1] * mat1[3][3] + mat1[3][1] *
                             mat1[2][3] * mat1[1][0])
            r4 = (mat1[1][0] * mat1[2][1] * mat1[3][2] + mat1[2][0] * mat1[3][1] * mat1[1][2] + mat1[1][1] * mat1[2][
                2] *
                  mat1[3][0]) - (
                             mat1[1][2] * mat1[2][1] * mat1[3][0] + mat1[3][1] * mat1[2][2] * mat1[1][0] + mat1[2][0] *
                             mat1[1][1] * mat1[3][2])
            r = mat1[0][0] * r1 - mat1[0][1] * r2 + mat1[0][2] * r3 - mat1[0][3] * r4
            print("---------------\n")
            print("Определитель = ", r)

        if m == n == 5:
            print("Введите матрицу -")
            for i in range(m):
                a = []
                for j in range(n):
                    a.append(int(input()))
                mat1.append(a)

            print("---------------\n")
            print("Результат = ", determinant(mat1))

        if m == n == 6:
            print("Введите матрицу -")
            for i in range(m):
                a = []
                for j in range(n):
                    a.append(int(input()))
                mat1.append(a)
            print("---------------\n")
            print("Результат = ", determinant(mat1))

        if m == n == 7:
            print("Введите матрицу -")
            for i in range(m):
                a = []
                for j in range(n):
                    a.append(int(input()))
                mat1.append(a)
            print("---------------\n")
            print("Результат = ", determinant(mat1))
    if k == 7:
        m = int(input("Введите количество столбцов -"))
        n = int(input("Введите количество строк -"))

        print("Введите матрицу -")
        for i in range(m):
            a = []
            for j in range(n):
                a.append(int(input()))
            mat1.append(a)
        luDecomposition(mat1, n)
print("Спасибо за использование нашего калькулятора")
input()
