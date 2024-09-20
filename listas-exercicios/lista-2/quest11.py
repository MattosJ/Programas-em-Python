numero1= float(input("Digite o número: "))
numero2= float(input("Digite o número: "))
numero3= float(input("Digite o número: "))

def quadrado (valor):
  return valor ** 2

somaDosQuadrados = quadrado(numero1) + quadrado(numero2) + quadrado(numero3)

print(somaDosQuadrados)