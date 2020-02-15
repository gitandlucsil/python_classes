def fib(n):
    """Fibonacci:
    Se n <= 1, fib(n) = 1
    Se n > 1, fib(n) = fib(n - 1) + fib(n - 2)
    Exemplos de uso:
    >>> fib(0)
    1
    >>> fib(1)
    1
    >>> fib(10)
    89
    >>> [ fib(x) for x in range(10) ]
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    """
    if not type(n) is int:
        raise TypeError

    if n > 1:
        return fib(n-1) + fib(n-2)
    else:
        return 1

def _doctest():
    import doctest
    doctest.testmod()

if __name__=="__main__":
    _doctest()
    