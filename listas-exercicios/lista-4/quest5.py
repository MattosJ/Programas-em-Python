maior = -99999999999999999999999999
menor =9999999999999999999999999999
for i in range(10):
  dado = float(input("Digite o número: "))
  if(dado <= menor):
    menor = dado
  if(dado >= maior):
    maior = dado
print(maior,menor)