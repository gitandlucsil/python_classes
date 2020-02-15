meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
while True:
    mes = int(input("Escolha um mes(1-12):"))
    if(1 <= mes <= 12):
        print("O mes é: "+meses[mes-1])
    else:
        print("Mes invalido")