arquivo1 = input("Digite o nome do arquivo1 :")
arquivo2 = input("Digite o nome do arquivo2 :")
abrirArq1 = open(arquivo1,"r")
abrirArq2 = open(arquivo2, "r")

conteudo1 = abrirArq1.read()
conteudo2 = abrirArq2.read()

abrirArq1.close()
abrirArq2.close()

novoArquivo = open("concactenarArquivos.txt" , "w")
conteudoNovo = novoArquivo.write(conteudo1)
novoArquivo.close()
novoArquivo2 = open("concactenarArquivos.txt" ,"a")
conteudoNovo2 = novoArquivo2.write(conteudo2)
novoArquivo2.close()
