lista = [23, 5, 87, 12, 45, 76, 3, 98, 34, 56, 18, 91, 67, 29, 42, 84, 10, 63, 73, 51, 
         27, 60, 36, 80, 99, 15, 8, 70, 94, 1, 49, 64, 21, 39, 6, 55, 31, 47, 89, 72, 
         33, 11, 59, 82, 14, 20, 93, 25, 68, 78, 17, 9, 40, 62, 2, 50, 37, 30, 7, 85, 
         46, 92, 16, 100, 4, 53, 13, 48, 65, 19, 41, 83, 75, 32, 58, 22, 71, 54, 28, 
         95, 38, 61, 66, 35, 81, 44, 74, 90, 26, 69, 79, 24, 57, 97, 43, 52, 88, 86, 
         77, 96]


def quickSort(lista):
  if len(lista) < 2:
    return lista
  else:
    pivo = lista[len(lista) - 1]
    menores = []
    maiores = []
    for i in range(len(lista) - 1):
      if(lista[i] <= pivo):
        menores.append(lista[i])
      else:
        maiores.append(lista[i])
  return quickSort(menores) + [pivo] + quickSort(maiores)


print(quickSort(lista))