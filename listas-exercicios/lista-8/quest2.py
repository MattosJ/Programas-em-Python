def vogal(caractere):
  letra = caractere.lower()
  if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    return True
  else:
    return False

arq = open("arq.txt","r")

conteudo = arq.read()

vogais = 0

for i in range(len(conteudo)):
  if(vogal(conteudo[i])):
    vogais += 1

print(vogais)