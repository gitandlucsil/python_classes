class Projetil(object):

    def __init__(self,alcance,tempo):
        self.alcance = alcance
        self.tempo = tempo
        self.velocidade = 0

    def set_velocidade(self,velocidade):
        self.velocidade = self.alcance/self.tempo

    def get_velocidade(self):
        return self.velocidade

    velocidade_p = property(get_velocidade,set_velocidade)

moab = Projetil(alcance=10000,tempo=60)

print(moab.velocidade_p)
moab.velocidade_p = 10
print(moab.velocidade_p)
moab.velocidade_p = 10
print(moab.velocidade_p)