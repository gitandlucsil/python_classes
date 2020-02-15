#lista = [ <expressão> for <referência> in <sequência> if <condição> ]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#Eleve os impares ao quadrado
print([x**2 for x in nums if x%2==1])
#Usando filter e map
impares_ao_quadrado = map(lambda x:x**2,filter(lambda x : (x%2==1),nums))
print(list(impares_ao_quadrado))