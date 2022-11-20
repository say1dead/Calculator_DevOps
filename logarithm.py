def ln(x):
    if x > 0:
        value = 10**10 * ((x ** (1/10**10)) - 1)
        return value
    else:
        return None


def log(x, base):
    if x > 0 and base > 0:
        value = ln(x) / ln(base)
        return value
    else:
        return None

