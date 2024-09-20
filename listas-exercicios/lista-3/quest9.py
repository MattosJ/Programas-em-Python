numero1 = int(input("Digite o número: "))
numero2 = int(input("Digite o número: "))
numero3 = 0
if(numero1 != numero2):
  numero3 = numero2
  numero2 = numero1
  numero1 = numero3
  print(numero1)
  print(numero2)
else:
  print("Numeros iguais!")