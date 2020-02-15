from numpy import arange, cos, sin
from scipy.signal import cspline1d, cspline1d_eval
from matplotlib.pyplot import plot, show

x0 = arange(20) #X original
print(x0)
y0 = cos(x0) * sin(x0/2) #Y a partir de X
print(y0)
dx = x0[0]-x0[1] #Diferença original
print(dx)
x1 = arange(-1,21,0.1)
print(x1)
#Coeficientes para arranjo de 1 dimensão
cj = cspline1d(y0)
print(cj)
# Avalia o Spline para um novo conjunto de pontos
y1 = cspline1d_eval(cj, x1, dx=dx,x0=x0[0])
#plot(x1, y1, '-g', x0, y0, '^y') # Desenha
#show() # Mostra o gráfico
plot(x0,y0,'-b',x0,y0,'^y')
show()
vet_teste = [0,1,2,3,4,5,6,7,8,9,10]
vet_teste2 = [0,1,4,9,16,25,36,49,64,81,100]
plot(vet_teste,vet_teste2,'-b',vet_teste,vet_teste2,'^y')
show()