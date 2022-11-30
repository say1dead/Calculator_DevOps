import unittest
def ln(x):
    if x > 0:
        value = 10 ** 8 * ((x ** (1 / 10 ** 8)) - 1)
        return value
    else:
        return None


def log(x, base):
    if x > 0 and base > 0:
        value = ln(x) / ln(base)
        return int(value)
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

def transpone(a):
    zip_row = zip(*a)
    b = [list(row) for row in zip_row]
    return b
    
class Test(unittest.TestCase):
    def test_sin(self):
      self.assertEqual(sin(90), 1.0)
    def test_cos(self):
      self.assertEqual(cos(180), -1.0)
    def test_log(self):
      self.assertEqual(log(32, 2), 5)
    def test_fact(self):
      self.assertEqual(factorial(10), 3628800)
    def test_transpon(self):
      self.assertEqual(transpone([[1,2,3],[4,5,6]]), [[1,4],[2,5],[3,6]])
unittest.main()
