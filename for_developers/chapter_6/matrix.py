import numpy

print("Criando uma matriz a partir de uma lista:")
a = [[3,4,5],[6,7,8],[9,0,1]]
Z = numpy.matrix(a)
print(Z)
print("Transposta da matriz:")
print(Z.T)
print("Inverda da matriz:")
print(Z.I)
#Criando outra matriz
b = numpy.matrix([[3],[2],[1]])
print("Multiplicando matrizes:")
print(a*b)
print("Resolvendo um sistema linear:")
print(numpy.linalg.solve(Z,numpy.array([0,1,2])))