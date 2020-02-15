import io
abrir = open("texte.txt","w")
abrir.close()
editar = open("texte.txt","a")
editar.write("Escrita no arquivo")
editar.close()
editar.closed
ler = open("texte.txt","r")
print(ler.readline())
ler.close()