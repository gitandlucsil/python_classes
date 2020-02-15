class Carro():

    def __init__(self,consumo):
        self.consumo = consumo
        self.combustivel = 0

    def abastecer(self,combustivel):
        self.combustivel = combustivel

    def gasolina(self):
        return self.combustivel

    def mover(self,km):
        litros_consumidos = km/self.consumo
        if(self.combustivel > litros_consumidos):
            self.combustivel = self.combustivel - litros_consumidos
        else:
            self.combustivel = 0
        return self.combustivel

gol = Carro(10)
gol.abastecer(50)
print(gol.gasolina())
print(gol.mover(200))