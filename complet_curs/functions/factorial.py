def factorial(num):
    f = 1
    while num > 1:
        f *= num
        num -= 1
    return f

def factorial_recursive(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial_recursive(num-1)

for index in range(100):
    print("Factorial of %s is: %s" % (index, factorial(index)))

for index in range(100):
    print("Factorial of %s is: %s" % (index, factorial(index)))

