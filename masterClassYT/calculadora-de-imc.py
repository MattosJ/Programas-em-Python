def imc():
  altura = float(input("Digite sua altura (ex: 1.75)"))
  peso = float(input("Digite seu Peso: ex: 70.40"))
  imc = peso / altura ** 2
  print(imc)
  if imc < 18.5:
    print("Magreza")
  if imc > 18.5 and imc < 24.9 :
    print("Normal")
  if imc > 25.0 and imc < 29.9:
    print("Sobrepeso")
  if imc > 29.9 and imc < 39.9:
    print("Obesidade")
  if imc > 39.9 :
    print("Obesidade Grave")
    
imc()