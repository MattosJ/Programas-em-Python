numero1 = int(input("Digite o número: "))
numero2 = int(input("Digite o número: "))
if(numero1 > numero2):
  print("O numero " + str(numero1) + " é o maior")
  if(numero1 % numero2 == 0):
    print("É multiplo")
  else:
    print("Não são multiplos!")
elif(numero2 > numero1):
  print("O numero " + str(numero2) + " é o maior")
  if(numero2 % numero1 == 0):
    print("É multiplo")
  else:
    print("Não são multiplos!")
else:
  print("Os números são iguais!")
 
