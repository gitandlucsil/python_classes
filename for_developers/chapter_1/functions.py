#1.Faca um programa, com uma funcao que necessite de tres argumentos, e que forneca a soma desses tres argumentos
print("----Inicio exercicio 1----")
def soma_tres_numeros(num1,num2,num3):
    return num1+num2+num3
print(soma_tres_numeros(1,1,1))
print(soma_tres_numeros(1,2,1))
print(soma_tres_numeros(1,1,2))
#2.Faca um programa, com uma funcao que necessite de um argumento. A funcao retorna o valor de caractere ’P’, se seu
#  argumento for positivo, e ’N’, se seu argumento for zero ou negativo
print("----Inicio exercicio 2----")
def positive_or_negative(argument):
    if argument > 0:
        return "P"
    elif argument <= 0:
        return "N"
print(positive_or_negative(1))
print(positive_or_negative(0))
print(positive_or_negative(-1))
print(positive_or_negative(343434434334434))