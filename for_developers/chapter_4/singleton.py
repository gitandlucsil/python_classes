class Singleton(type):

    def __init__(cls,name,bases,dic):
        type.__init__(cls,name,bases,dic)
        #Retorna o próprio objeto na cópia
        def __copy__(self):
            return self
        #Retorna o próprio objeto na cópia recursiva
        def __deepcopy__(self,memo=None):
            return self

        cls.__copy__=__copy__
        cls.__deepcopy__=__deepcopy__

    def __call__(cls,*args,**kwargs):
        #Chamda que cria noso objetos, aqui retorna sempre o mesmo
        try:
            return cls.__instance
        #Se __instance não existir, então crie...
        except AttributeError:
            #A função super() pesquisa na MRO a partir de Singleton
            cls.__instance = super(Singleton,cls).__call__(*args, **kwargs)
            return cls.__instance

class Log(object):
    #Define a metaclase desta classe
    __metaclass__ = Singleton

    def __init__(self):
        #Abre o arquivo de log para escrita
        self.log = open("msg.log","w")
        #Sempre será usado o mesmo objeto do arquivo
    
    def write(self,msg):
        print(msg)
        #Acrescenta as mensagens no arquivo
        self.log.write(str(msg)+"\n")

    def set_valor(self,valor=10):
        self.valor = valor
    
    def get_valor(self):
        try:
            return self.valor
        except:
            return 0

log = Log()
log.set_valor(10)
log.write("Teste 2")
print(log.get_valor())
log2 = Log()
log2.write("Teste 3")
print(log2.get_valor())
#Log().write("Teste 1")