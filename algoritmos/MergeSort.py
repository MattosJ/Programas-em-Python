lista = [12, 5, 23, 9, 27, 1, 17, 14, 6, 28, 3, 22, 19, 8, 13, 16, 25, 4, 10, 7, 11, 24, 18, 29, 2, 15, 20, 0, 26, 21]

def mergeSort(arr):
  if(len(arr) <= 1):
    return arr
  mid = len(arr) //2
  direita = arr[mid:]
  esquerda = arr[:mid]

  direitaOrdenada = mergeSort(direita)
  esquerdaOrdenada = mergeSort(esquerda)
  return merge(esquerdaOrdenada,direitaOrdenada)


def merge(esquerda,direita):
  resultado = []
  i = j = 0

  while i < len(esquerda) and j < len(direita) :
    if esquerda[i] < direita[j]:
      resultado.append(esquerda[i])
      i += 1
    else:
      resultado.append(direita[j])
      j += 1
  
  resultado.extend(esquerda[i:])
  resultado.extend(direita[j:])

  return resultado


print(mergeSort(lista))