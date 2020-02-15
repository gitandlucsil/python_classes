class Pendrive(object):

    def __init__(self,tamanho,interface="2.0"):
        self.tamanho = tamanho
        self.interface = interface
#A classe MP3Player é derivada da classe Pendrive
class MP3Player(Pendrive):
    def __init__(self,tamanho,interface="2.0",turner=False):
        self.turner = turner
        Pendrive.__init__(self,tamanho,interface)

mp3 = MP3Player(1024)
print("%s\n%s\n%s\n" % (mp3.tamanho,mp3.interface,mp3.turner))