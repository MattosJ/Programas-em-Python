nomeArquivo = input("Digite o nome do arquivo: ")
arq = open(nomeArquivo, "r")
conteudo = arq.read()
arq.close()
novoArquivo = open("novoArquivo.txt" , "w")
conteudoNovoArquivo = novoArquivo.write(conteudo.upper())