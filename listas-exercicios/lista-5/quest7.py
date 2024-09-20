lista = []
for i in range(10):
  item = int(input("Digite o número: "))
  lista.append(item)
numerosImpressos = []
for i in range(len(lista)):
  if(i== 0):
    print(lista[i])
    numerosImpressos.append(lista[i])
  else:
    naLista = False
    j = 0
    while j < len(numerosImpressos):
      if(lista[i] == numerosImpressos[j]):
          naLista = True
          break
      j+=1
    if(naLista == False):
      print(lista[i])
      numerosImpressos.append(lista[i])