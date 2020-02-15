#1.Faca um dicionario que contenha suas refeicoes e um alimento que esteja contido em cada uma delas. Imprima na tela.
#  Apos isso, mude os alimentos pelos seus alimentos favoritos
print("----Inicio exercicio 1----")
refeicao = {
    "cafe_da_manha" : "banana",
    "almoco" : "feijao",
    "janta" : "frango"
}
print(refeicao.keys())
print(refeicao.values())
print(refeicao.items())
refeicao["cafe_da_manha"] = "sushi"
refeicao["almoco"] = "churrasco"
refeicao["janta"] = "churrasco"
print(refeicao.keys())
print(refeicao.values())
print(refeicao.items())
#2. Faca um dicionario que contenha os meses do ano e um aniversariante por mes. Apos, pergunte ao usuario um aniversariante
#   por mes e troque os valores do seu calendario de aniversario pelos do usuario
print("----Inicio exercicio 2----")
aniversario = {
    "Janeiro" : "Joao",
    "Fevereiro" : "Maria",
    "Marco" : "Marcos"
}
for item in aniversario:
    aniversariante = input("Informe um aniversariante para "+item+": ")
    aniversario[item] = aniversariante
print(aniversario.keys())
print(aniversario.values())
print(aniversario.items())
