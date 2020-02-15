import cProfile

def fib_recursivo(n):
    if n > 1:
        return fib_recursivo(n-1) + fib_recursivo(n-2)
    else:
        return 1

def fib_loop(n):
    if n > 1:
        fibs = {0:1,1:1}
        for i in range(2,n+1):
            fibs[i] = fibs[i-1]+fibs[i-2]
        return fibs[n]
    else:
        return 1

print("fib_recursivo")
cProfile.run("[fib_recursivo(x) for x in range(1,31)]")
print("fib_loop")
cProfile.run("[fib_loop(x) for x in range(1,31)]")