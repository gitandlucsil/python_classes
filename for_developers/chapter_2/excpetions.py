import random
import io

try:
    print(1/0)
except ZeroDivisionError:
    print("Erro ao tentar dividir por zero!")

# Cria um arquivo com 25 números randômicos
with open("temp.txt","w") as temp:
    for y in range(5):
        for x in range(5):
            # Grava a saída do comando no arquivo indicado
            print(temp,"%.2f" % random.random())
        print(temp)
# Exibe o conteúdo do arquivo
with open("temp.txt") as temp:
    print(temp.readline())
# Fora dos blocos, o arquivo está fechado
# Isso gera uma exceção ValueError: I/O operation on closed file
print(temp)