#Recursive factorial
def factorial_recursive(num):
    if num <= 1:
        return 1
    else:
        return (num * factorial_recursive(num -1))

print("\nRecursive factorial: \n")
for index in range(1,10):
    print(factorial_recursive(index))

#Non recursive factorial
def factorial_non_recursive(num):
    aux = 1
    for index in range(1,num+1):
        aux = aux * index
    return aux

print("\nNon-Recursive factorial: \n")
for index in range(1,10):
    print(factorial_non_recursive(index))

