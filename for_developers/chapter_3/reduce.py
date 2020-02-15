import functools

#Soma com reduce
nums = range(10)
print(functools.reduce(lambda x,y: x+y,nums))
#Concatenar string
palavras = ["Bom","dia","tudo","bem"]
print(functools.reduce(lambda x,y:x+y,palavras))
#Fatorial
def fat(n):
    return functools.reduce(lambda x,y:x*y,range(1,n))

print(fat(6))


