maior = -99999999999999999
posicao = -2
lista1 = []
for i in range(4):
  dado = int(input(""))
  lista1.append(dado)
for i in range(len(lista1)):
  if(lista1[i] > maior):
    maior = lista1[i]
    posicao = i


print(maior)
print(posicao)