# Colhendo algumas informações dos objetos globais no programa
from types import ModuleType

def info(n_obj):
    #Cria uma referência ao objeto
    obj = globals()[n_obj]
    #Mostra as informações sobre o objeto
    print("Nome do objeto: ",n_obj)
    print("Identificador: ",id(obj))
    print("Tipo: ",type(obj))
    print("Representação: ",repr(obj))
    #Se for um módulo
    if isinstance(obj, ModuleType):
        print("itnes: ")
        for item in dir(obj):
            print(item)

#Mostrando as informações
for n_obj in dir():
    info(n_obj)