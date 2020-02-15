class User(object):

    def __init__(self,name):
        self.name = name
    
#Um novo método para a classe
def set_password(self,password):
    self.password = password

def get_password(self):
    return self.password

print("Classe original: ",dir(User))
#Inserir novo método na classe
User.set_password = set_password
User.get_password = get_password
print("Classe modificada: ",dir(User))

user = User("convidado")
user.set_password("convidado")
print("Objeto: ",dir(user))
print("Nome: ",user.name)
print("Senha: ",user.get_password())