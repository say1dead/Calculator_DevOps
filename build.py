unit test:

import unittest
import calc1
class Test(unittest.TestCase):
    def test_sin(self):
      self.assertEqual(calc1.sin(90), 1.0)
    def test_cos(self):
      self.assertEqual(calc1.cos(180), -1.0)
    def test_log(self):
      self.assertEqual(calc1.log(32, 2), 5)
    def test_fact(self):
      self.assertEqual(calc1.factorial(10), 3628800)
    def test_transpon(self):
      self.assertEqual(calc1.transpone([[1,2,3],[4,5,6]]), [[1,4],[2,5],[3,6]])
if name == 'main':
    unittest.main()
