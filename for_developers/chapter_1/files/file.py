import sys
import os

#Criando um objeto do tipo file
temp = open("temp.txt","w")
#Escrevendo no arquivo
for index in range(10):
    temp.write("%02d\n"%index)
#Fechando
temp.close()
#Lendo o arquivo
tempo = open("temp.txt")
print(tempo)
for linha in tempo:
    print(linha)
print(open("temp.txt").readlines())

print(os.path.basename("temp.txt"))
print(os.path.dirname("temp.txt"))
print(os.path.exists("temp.txt"))
print(os.path.getsize("temp.txt"))

