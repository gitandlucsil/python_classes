def gen_pares():
    i = 0
    for i in range(0,20,2):
        i += 2
        yield i
# Mostra cada número e passa para o próximo
for n in gen_pares():
    print(n)



lista = ["A","B","C","D","E"]
def gen_listas():
    for item in lista:
        yield item
# Mostra cada item da lista
for n in gen_listas():
    print(n)
