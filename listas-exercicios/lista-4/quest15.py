limiteInferior = int(input("Digite o número do limite inferior: "))
limiteSuperior = int(input("Digite o número do limite Superior: "))
if(limiteInferior > limiteSuperior):
  print("Intervalo Inválido!")
  limiteInferior = int(input("Digite o número do limite inferior: "))
  limiteSuperior = int(input("Digite o número do limite Superior: "))

impares = 0
for i in range(limiteInferior,limiteSuperior+1):
  if(i % 2 != 0):
    impares += i
print(impares)