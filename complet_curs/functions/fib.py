def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)

for index in range(100):
    print("Fibonacci of %s is: %s" % (index, fibonacci(index)))
