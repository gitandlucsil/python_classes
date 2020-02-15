import numpy

#Criando arranjos
print ("Arranjo criado a partir de uma lista:")
a = numpy.array([0,1,2,3,4,5,6,7,8])
print(a)
print("Arranjo criado a partir de um intervalo")
b = numpy.arange(0.,4.5,.5)
print(b)
print("Arranjo de 1s 2x3")
c = numpy.ones((2,3))
print(c)
print("Arranjos podem gerar novos arranjos:")
# numpy.round() é uma função do numpy
# semelhante ao builtin round(), porém aceita
# arranjos como parâmetro
cos = numpy.round(numpy.cos(b),1)
print(cos)
print("Multiplicando cada elemento por um escalar:")
print(5*b)
print("Somando arranjos elemnto por elemento:")
print(b+cos)
print("Redimensionando o arranjo:")
b.shape = 3,3
print(b)
print("Arranjo transposto:")
print(b.transpose())
print("Achata o arranjo:")
print(b.flatten())
print("O acesso aos elementos funciona como nas listas:")
print(b[1])
print("Caso especial, diferente da lista:")
print(b[1,1])
#Dados sobre o arranjo
print("Formato do arranjo:")
print(b.shape)
print("Quantidade de eixos:")
print(b.ndim)
print("Tipo dos dados:")
print(b.dtype)