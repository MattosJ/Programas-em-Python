lista1 = []
lista2 = []
lista3 = []
n = int(input("Digite o Tamanho das listas: "))
while n <=  0:
  n = int(input("Digite o Tamanho das listas: "))
somatorio1 = 0
somatorio2 = 0
for i in range(n):
  dado = float(input("Digite o número da lista 1: "))
  dado2= float(input("Digite o número da lsita 2: "))
  lista1.append(dado)
  lista1.append(dado2)
  somatorio1 += dado
  somatorio2 += dado2
  lista3.append(dado + dado2)

medialista1 = somatorio1 / n
medialista2 = somatorio2/n
if(medialista1 > medialista2):
  print("A média da lista 1 é maior: "+str(medialista1)+", "+str(medialista2))
elif(medialista1 < medialista2):
  print("A média da lista 2 é maior: "+str(medialista2)+", "+str(medialista1))
else:
  print("As duas listas tem médias iguais: "+str(medialista1)+", "+str(medialista2))

for i in range(n):
  print(lista3[i])