class Classe():
    """
    Isto é uma classe
    """
    clsvar = []

    def __init__(self,args):
        '''
        Inicializador da classe
        <bloco de codigo>
        '''
    def __done__(self):
        '''
        Destrutor da classe
        <bloco de codigo>
        '''
    def metodo(self,params):
        '''
        Método do objeto
        <bloco de codigo>
        '''   
    @classmethod
    def class_method(cls,params):
        '''
        Método da classe
        <bloco de codigo>
        '''          
    @staticmethod
    def static_method(params):
        '''
        Método estático
        <bloco de codigo>
        '''   

obj = Classe("")
obj.metodo("")
Classe.class_method("")
Classe.static_method("")