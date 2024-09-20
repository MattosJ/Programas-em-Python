lista = []
maior = -99999999999999999
for i in range(5):
  valor = int(input("Digite o número: "))
  lista.append(valor)
  if(valor > maior):
    maior = valor

print(maior)