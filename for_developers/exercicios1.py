'''
1. Implementar duas funções:
▪ Uma que converta temperatura em graus Celsius para Fahrenheit.
▪ Outra que converta temperatura em graus Fahrenheit para Celsius.
'''
def celsius_to_fahrenheit(temperatura):
    return (5/9 * temperatura) - 17.7

def fahrenheit_to_celsius(temperatura):   
    return (9/5 * temperatura) + 32

print(fahrenheit_to_celsius(10))
print(fahrenheit_to_celsius(20))
print(fahrenheit_to_celsius(22.5))
print(celsius_to_fahrenheit(50))
print(celsius_to_fahrenheit(68))
print(celsius_to_fahrenheit(72.5))
'''
2. Implementar uma função que retorne verdadeiro se o número for primo
(falso caso contrário). Testar de 1 a 100.
'''
def verifica_primo(numero):
    resultado = False
    for index in range (2,int((numero/2))):
        if(numero%index == 0):
            resultado = True
            break
    if(resultado):
        print("não é primo!")
    else:
        print(" é primo!")

for index in range(1,100):
    print("O número %d ",(index))
    verifica_primo(index)
'''
5. Escreva uma função que:
▪ Receba uma frase como parâmetro.
▪ Retorne uma nova frase com cada palavra com as letras invertidas.
'''
frase = input("Digite uma frase:")
print(frase)
palavras = frase.split(" ")
print(palavras)
nova_frase = ""
for palavra in palavras:
    #print(palavra[::-1])
    nova_frase += palavra[::-1]+" "
print(nova_frase)
