lista = []
positivos = 0
negativos = 0
for i in range(10):
  numero = float(input("Digite o número: "))
  lista.append(numero)
  if(numero >= 0):
    positivos += 1
  else:
    negativos += 1
print(positivos)
print(negativos)