lista = [34, 87, 12, 65, 29, 73, 51, 19, 98, 46, 5, 77, 32, 61, 15, 40, 22, 93, 58, 11]

def buscaMenor(arr):
  menor = arr[0]
  menor_indice = 0
  for i in range(1,len(arr)):
    if arr[i] < menor:
      menor = arr[i]
      menor_indice = i
  return menor_indice


def selectionSort(arr):
  novoArr = []
  for i in range(len(arr)):
    menor = buscaMenor(arr)
    novoArr.append(arr.pop(menor))
  return novoArr


print(selectionSort(lista))