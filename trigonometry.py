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
    x = x + x**3/6 + 3*x**5/40 + 5*x**7/112 + 35*x**9/1152 + 81*x**11/2816 + 231*x**13/13312
    return x
