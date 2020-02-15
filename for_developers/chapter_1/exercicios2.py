#1.Exibir uma serie de numeros (1, 2, 3, 4, 5, ... ) em um loop infinito. O programa deve encerrar-se quando for pressionada
#  uma tecla especıfica, como um ESC
print("----Inicio exercicio 1----")
i = 0
while True:
    i=i+1
    print(i)
    if(input("") == ""):
        break 
#2. Obter uma serie de numeros do teclado e ordena-las tanto em ordem ascendente como descendente
print("----Inicio exercicio 2----")
numero = 0
numeros = []
while(numero != -1):
    numero = int(input("Infome um numero: "))
    if(numero != -1):
        numeros.append(numero)
print("\nLista: ",numeros)
print("\nCrescente:",sorted(numeros))
print("\nDescrescente:",sorted(numeros, reverse=True))
#3. Faca um Programa que peca 2 numeros inteiros e um numero real. Calcule e mostre:
#   a - O produto do dobro do primeiro com metade do segundo
#   b - A soma do triplo do primeiro com o terceiro
#   c - O terceiro elevado ao cubo
print("----Inicio exercicio 3----")
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))
resultado_a = float((num1*2)*(float(num1/2.0)))
print("Resultado_a: ",resultado_a)
resultado_b = (num1*3) + num3
print("Resultado_b: ",resultado_b)
resultado_c = num3**3
print("Resultado_c: ",resultado_c)
#4.  Faca um programa que receba dois numeros inteiros e gere os numeros inteiros que estao no intervalo compreendido por eles
print("----Inicio exercicio 4----")
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
numeros = range(num1,num2)
for numero in numeros:
    print(numero)
