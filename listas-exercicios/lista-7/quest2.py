### Escreva uma função que calcula e retorna a soma dos números de 1 até N (número inteiro positivo) usando recursão.
###Por exemplo: a soma de 1 até 5 retorna 15
def somarNumeros(n):
  if n == 1:
    return 1
  else:
    return n + somarNumeros(n-1)
  
print(somarNumeros(5))