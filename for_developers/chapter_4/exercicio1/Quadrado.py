class Quadrado():

    def __init__(self,lado):
        self.lado = lado

    def set_lado(self,lado):
        self.lado = lado

    def get_lado(self):
        return self.lado

    def calcula_area(self):
        return self.lado * self.lado


quad1 = Quadrado(5)
print(quad1.get_lado())
print(quad1.calcula_area())
quad1.set_lado(10)
print(quad1.get_lado())
print(quad1.calcula_area())
