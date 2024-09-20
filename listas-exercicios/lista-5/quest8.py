a = []
b = []
c = []

for i in range(10):
  dado = int(input("Digite o número para A: "))
  dadoB = int(input("Digite o número para B: "))
  a.append(dado)
  b.append(dadoB)
  c.append(dado - dadoB)

for i in range(len(c)):
  print(c[i])