arq = open("arq.txt", "r")
encontraLetra = input("Digite a letra que você quer encontrar no arquivo: ")
letraAparece = 0
conteudo = arq.read()
arq.close()
for i in range(len(conteudo)):
  if(conteudo[i].lower() == encontraLetra ):
    letraAparece += 1
print(letraAparece)