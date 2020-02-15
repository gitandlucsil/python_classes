import timeit


# Com Generator Expression
cod = 'list(x ** 2 for x in range(1, 1001))'
print(timeit.Timer(cod).timeit())
# Com List Comprehesion
cod = '[x ** 2 for x in range(1, 1001)]'
print(timeit.Timer(cod).timeit())