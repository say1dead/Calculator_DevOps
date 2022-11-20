def ln(x):
    value = 10**10 * ((x ** (1/10**10)) - 1)
    return value


def log(x, base):
    value = ln(x) / ln(base)
    return value
