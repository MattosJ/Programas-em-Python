lista = []
def quadrado(valor):
  return valor **2

for i in range(10):
  valor = float(input("Digite o número: "))
  valorAoquadrado = quadrado(valor)
  lista.append(valorAoquadrado)
for i in range(10):
  print(lista[i])