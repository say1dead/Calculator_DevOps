import numpy as np


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
    x *= 3.1415926/180
    value = x
    sign = -1
    for i in range(3, 100, 2):
        value += (x**i / factorial(i) * sign)
        sign *= -1
    return round(value, 4)


def cos(x):
    x *= 3.1415926/180
    value = 1
    sign = -1
    for i in range(2, 100, 2):
        value += (x**i / factorial(i) * sign)
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


#  + 429*x**15/30720
def arcsin(x):
    if -1 <= x <= 1:
        x = x + x**3/6 + 3*x**5/40 + 5*x**7/112 + 35*x**9/1152 + 81*x**11/2816 + 231*x**13/13312 + 429*x**15/30720
        return x
    else:
        return None

def arccos(x):
    if -1 <= x <= 1:
        x = 3.141592653589793238/2 - arcsin(x)
        return x
    else:
        return None

def arctg(x):
    x = arcsin(x / ((1 + x ** 2) ** 0.5))
    return x


k = int(input(
    "В каком модуле хотите выполнять вычисления:\n1. Простые вычисление.\n2. Тригонометрия.\n3. Матрицы.\nВаш выбор - "))
print("--------------\n")
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
    k = int(input("Что хотим посчитать:\n1. Синус.\n2. Косинус.\n3. Тангенс.\n4. Котангенс."
                  "\n5. Арксинус.\n6. Арккосинус.\n7. Арктангесн.\n8. Арккотангенс.\nВаш выбор - "))
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
    print("Все еще скоро добавим матрицы ¯\_(ツ)_/¯")
