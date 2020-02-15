import time

# localtime() Retorna a data e hora local no formato
# de uma estrutura chamada struct_time, que é uma
# coleção com os itens: ano, mês, dia, hora, minuto,
# segundo, dia da semana, dia do ano e horário de verão
print(time.localtime())
# asctime() retorna a data e hora como string, conforme
# a configuração do sistema operacional
print(time.asctime())
# time() retorna o tempo do sistema em segundos
ts1 = time.time()
# gmtime() converte segundos para struct_time
tt1 = time.gmtime(ts1)
print(ts1, "->", tt1)
# Somando uma hora
tt2 = time.gmtime(ts1 + 3600.)
# mktime() converte struct_time para segundos
ts2 = time.mktime(tt2)
print(ts2, '->', tt2)
# clock() retorna o tempo desde quando o programa iniciou, sem segundos
print("O programa levou ",time.clock()," segundos até agora")
#Contado os segundos
for index in range(5):
    time.sleep(1)
    print(index,"segundos(s)")
    print("O programa levou ",time.clock()," segundos até agora")