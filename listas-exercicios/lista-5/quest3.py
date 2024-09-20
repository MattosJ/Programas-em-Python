lista = []

for i in range(10):
  numero = float(input("Digite o número: "))
  lista.append(numero)


x = int(input("Digite o índice: "))
y = int(input("Digite o índice: "))

while((x > 9 ) or (y>9)):
  print("índices inválidos")
  x = int(input("Digite o índice: "))
  y = int(input("Digite o índice: "))


print(lista[x] + lista[y])