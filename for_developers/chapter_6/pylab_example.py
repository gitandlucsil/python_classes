from pylab import *
from numpy import arange, cos, sin
from matplotlib.pyplot import plot, show, title, grid, xlabel, ylabel

entrada = arange(0.,20.1,.1)
print(entrada)
#Calcula os cossenos da entrada
saida = cos(entrada)
print(saida)
#Plota a curva
plot(entrada,saida)
#Texto para os eixos
xlabel("Entrada")
ylabel("Cosseno")
#Texto para o topo da figura
title("Cossenos")
#Ativa a grade
grid(True)
show()