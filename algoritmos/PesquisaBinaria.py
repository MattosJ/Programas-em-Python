
lista = [10,9,8,75,432,45,76,12,30,10,6,5,4,3,10,9,18,79,52,0,8]
lista.sort()

def PesquisaBinaria(lista,elemento):
  tamanho = len(lista) - 1
  itemMenor = 0
  
  while itemMenor <= tamanho:
    meio = (itemMenor + tamanho) // 2
    chute = lista[meio]
    if(chute == elemento) :
      return meio
    if(chute < elemento):
      itemMenor = meio + 1
    else:
      tamanho = meio - 1

  return None

print(PesquisaBinaria(lista,30))