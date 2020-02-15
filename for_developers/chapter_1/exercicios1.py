#1.Faca um programa que leia um vetor de 5 numeros inteiros e mostre-os.
print("----Inicio exercicio 1----")
vetor = range(0,5)
for elemento in vetor:
    print(elemento)

#2. Faca um programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores
#   deverao ser compostos pelos elementos intercalados dos dois outros vetores
print("----Inicio exercicio 2----")
vetor1 = range(0,20,2)
vetor2 = range(1,21,2)
for elemento in vetor1:
    print(elemento)
for elemento in vetor2:
    print(elemento)
vetor3 = []
for indice in range(10):
    vetor3.append(vetor1[indice])
    vetor3.append(vetor2[indice])
print("\nTamanho do vetor 3: ",len(vetor3))
print("\nVetor 3: ",vetor3)
#3. Faca um programa que leia 4 notas, mostre as notas e a media na tela
print("----Inicio exercicio 3----")
nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))
nota3 = int(input("Digite a nota 3: "))
nota4 = int(input("Digite a nota 4: "))
media = (float((nota1+nota2+nota3+nota4)/4))
print("\n--NOTAS--")
print("N1: ",nota1)
print("N2: ",nota2)
print("N3: ",nota3)
print("N4: ",nota4)
print("\n--MEDIA--")
print("MEDIA: %.2f"%(media))

#4. Faca um programa que leia um numero indeterminado de valores, correspondentes a notas, encerrando a entrada de dados
#   quando for informado um valor igual a -1 (que nao deve ser armazenado). Apos esta entrada de dados, faca:
#   a - Mostre a quantidade de valores que foram lidos
#   b - Exiba todos os valores na ordem em que foram informados, um ao lado do outro
#   c - Calcule e mostre a media dos valores
#   d - Calcule e mostre a quantidade de valores acima da media calculada
#   e - Encerre o programa com uma mensagem
print("----Inicio exercicio 4----")
nota = 0
notas = []
while(nota != -1): 
    nota = int(input("Informe uma nota: "))
    if(nota != -1):
        notas.append(nota)
print("\nTerminado entrada de dados!")
print("\nQuantidade de notas lidas:",len(notas))
print("\nNotas: ",notas)
total = 0
media = 0
for nota in notas:
    total += nota
media = float(total/len(notas))
print("\nMedia: %.2f"%(media))
print("\nPrograma encerrado com sucesso!")