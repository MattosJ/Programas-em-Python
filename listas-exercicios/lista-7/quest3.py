###Escreva uma função para printar os elementos de uma lista usando recursão. Os elementos devem ser impressos a partir da primeira posição.
###Por exemplo: para o vetor {4, 3, 2, 9, 1} , a função deve imprimir 4 3 2 9 1

def imprimirVetor(lista):
  if len(lista) == 1:
    print(lista[0])
    return 
