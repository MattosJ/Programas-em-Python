def palavras_iguais(palavra1,palavra2):
  if palavra1 == palavra2:
    return True
  else:
    return False


arq = open("arq.txt", "r")

conteudo = arq.read()
arq.close()

palavra = input("Digite uma palavra: ")
ListaPalavras = conteudo.split(" ")
quantidade = 0
for i in range(len(ListaPalavras)):
  if palavras_iguais(palavra,ListaPalavras[i]):
    quantidade += 1

print(quantidade)