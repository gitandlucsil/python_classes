def decorator(f):
    f.decorated = True
    return f

@decorator
def func(arg):
    return arg

#Função decorada
def dumpargs(f):
    #Função que envolverá a outra
    def func(*args):
        #Mostra os argumentos passados para a função
        print(args)
        #Retornar o resultado da função original
        return f(*args)
    #Retorna a função modificada
    return func

@dumpargs
def multiply(*nums):
    m = 1
    for n in nums:
        m = m * n
    return m

print(multiply(1,2,3))