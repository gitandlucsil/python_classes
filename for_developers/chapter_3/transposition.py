from string import ascii_lowercase
#Uma lista com ("a",1), ("b",2)
print(list(zip(ascii_lowercase,range(1,100))))
#Transposta de uma matriz
matriz = [[1,2,3],[4,5,6],[7,8,9]]
print(list(zip(*matriz)))