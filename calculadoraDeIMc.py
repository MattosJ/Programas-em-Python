def dividir(a,b):
  return a / b


def calcquadrado(b):
  return b ** 2


def imc(peso,altura):
  return dividir(peso,calcquadrado(altura))


def indice(imc):
  if imc < 16.9:
    print('Muito abaixo da peso')
  elif imc > 16.9 and imc < 18.4:
    print('Abaixo do peso')
  elif imc > 18.4 and imc < 24.9:
    print('Peso normal')
  elif imc > 24.9 and imc < 29.9:
    print('Acima do peso')
  elif imc > 29.9 and imc < 34.9:
    print('Obesidedade grau 1')
  elif imc > 34.9 and imc < 40.1:
    print('Obesidade grau 2')
  elif imc > 40 :
    print('Obesidade grau 3')
    
    
def main():
  repetir = 0
  while repetir == 0:
    peso = float(input("Digite seu peso: "))
    altura = float(input("Dgite sua altura em metros (1.75): "))
    print("Seu imc: " + str(round(imc(peso,altura),2)))
    (indice(imc(peso,altura)))
    repetir = int(input("Fazer de novo -- 0 "))

main()