nums = [1,2,3,4,5,6,7,8,9,10,11,12]

#Selecionando os pares
pares = filter(lambda x : (x%2==0),nums)
print(list(pares))
#Selecionando os impares
impares = filter(lambda x : (x%2==1),nums)
print(list(impares))