import unittest

def fib(n):
    if not type(n) is int:
        raise TypeError

    if n > 1:
        return fib(n-1) + fib(n-2)
    else:
        return 1

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)
    def test0(self):
        self.assertEqual(fib(0), 1)
    def test1(self):
        self.assertEqual(fib(1), 1)
    def test10(self):
        self.assertEqual(fib(10), 89)
    def testseq(self):
        fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        for x, y in zip(fibs, [ fib(x) for x in self.seq ]):
            self.assert_(x is y)
    def testtype(self):
        self.assertRaises(TypeError,fib,"")

if __name__ == "__main__":
    unittest.main()