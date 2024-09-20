arq = open("arq.txt","w")

conteudo = input("Digite uma sequência de caracteres: ")

arq.write(conteudo)
arq.close()

arq = open("arq.txt", "r")

conteudo = arq.read()

print(conteudo)

arq.close()