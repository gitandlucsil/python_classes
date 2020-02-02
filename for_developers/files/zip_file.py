import zipfile

#Cria um zip novo
zip = zipfile.ZipFile("arq.zip","w",zipfile.ZIP_DEFLATED)
#Escreve uma string no zip como se fosse um arquivoEscreve uma string no zip como se fosse um arquivo
zip.writestr("texto.txt","abcabc")
zip.writestr("texto2.txt","def")
#Fecha o arquivo zip
zip.close()
#Abre o arquivo zip para leitura
zip = zipfile.ZipFile("arq.zip")
#Pega a lista dos arquivos compactados
arqs = zip.namelist()
for arq in arqs:
    #Mostra o nome do arquivo
    print("Arquivo",arq)
    #Pegando informações do arquivo
    zipinfo = zip.getinfo(arq)
    print("Tamanho original: ",zipinfo.file_size)
    print("Tamanho comprimido",zipinfo.compress_size)
    #Mostra o conteúdo dos arquivos
    print(zip.read(arq))