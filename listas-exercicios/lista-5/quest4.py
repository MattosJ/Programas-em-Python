lista = []
impares = []
for i in range(10):
  numero = int(input("Digite o número: "))
  lista.append(numero)
  if(numero % 2 != 0):
    impares.append(numero)
print(len(impares))