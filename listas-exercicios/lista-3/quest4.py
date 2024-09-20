numero1 = int(input("Digite o número: "))
numero2 = int(input("Digite o número: "))
if(numero1 > numero2):
  print("O numero " + str(numero1) + " é o maior")
  print("A diferença entre eles é:",numero1 - numero2)
elif(numero2 > numero1):
  print("O numero " + str(numero2) + " é o maior")
  print("A diferença entre eles é:",numero2 - numero1)
else:
  print("Os números são iguais!")
  print("A diferença entre eles é: 0")

