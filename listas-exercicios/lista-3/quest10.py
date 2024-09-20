numero = int(input("Digite o número: "))
if((numero % 3 == 0) and (numero % 5 == 0)):
  print("É divisível por 3 e por 5")
elif(numero % 5 == 0):
  print("É divisível por 5")
elif(numero % 3 == 0):
  print("É divisível por 3")
else:
  print("Não é divisível nem por 3 nem por 5")
