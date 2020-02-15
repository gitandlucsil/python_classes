import os
import time
import threading

class Monitor(threading.Thread):
    #Classe de monitoramento usando threads
    def __init__(self,ip):
        #Construtor da thread
        self.ip = ip
        self.status = None
        #Inicializador da classe Thread
        threading.Thread.__init__(self)

    def run(self):
        #Código que será executado pela Thread
        ping = os.popen("ping -n 1 %s"%self.ip).read()
        if "Esgotado" in ping:
            self.status = False
        else:
            self.status = True

if __name__ == "__main__":
    #Cria uma lista com um objeto de thread para cada IP
    monitores = []
    for index in range(1,255):
        ip = "10.10.10.%d" % index
        monitores.append(Monitor(ip))
    #Executa as Threads
    for monitor in monitores:
        monitor.start()

    #A thread principal continua enquanto as outras threads executam o ping para os endereços da lista
    #Verifque a cada segundo se as threads acabaram
    ping = True
    while ping:
        ping = False
        for monitor in monitores:
            if monitor.status == None:
                ping = True
                break 
        time.sleep(1)
    #Imprime os resultados no final
    for monitor in monitores:
        if monitor.status:
            print("%s no ar" % monitor.ip)
        else:
            print("%s fora do ar" % monitor.ip)