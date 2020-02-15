from numpy import arange, cos, sin
from scipy.signal import cspline1d, cspline1d_eval
from matplotlib.pyplot import plot, show, subplot, legend, bar, savefig

#Dados
ent1 = arange(0.,7.,.1)
sai1 = cos(ent1)
sai2 = sin(ent1)
dif = sai2 - sai1
# Divide a figura em 2 linhas e 1 coluna, e seleciona a parte superior
subplot(2,1,1)
# Plota a curva
# Primeira curva: ent1, sai1, 'bo:'
# Segunda curva: ent1, sai2, 'g^-'
plot(ent1, sai1, 'bo:', ent1, sai2, 'g^-')
# Cria uma legenda
legend(['Cossenos', 'Senos'])
# Seleciona a parte inferior
subplot(212)
# Desenha barras
# Eixo X: arange(len(dif)) + .5
# Eixo Y: dif
# Largura das barras: .5
# Cor: #ccbbaa
bar(arange(len(dif)) + .5, dif, .5, color='#ccbbaa')
# Salva a figura
savefig('graf.png')