def somar(a,b) :
  return a + b


def subtrair(a,b):  
  return a - b


def multiplicar(a,b) :   
  return a * b


def dividir(a,b) :   
  return a / b


def potencia(a,b):  
  return a ** b


def raiz(a,b):    
  return a ** (1/b)


def menu() :
  print("Operações:")
  print("Sair 0")
  print("Somar 1")
  print("Subtrair 2")
  print("multiplicar 3")
  print("Dividirr 4")
  print("Potenciação 5")
  print("Radiciação 6\n")


def main():
  funcs = [somar, subtrair, multiplicar, dividir, potencia, raiz]
  operacoes = ['+', '-', '*', '/', '^', 'na raiz']

  menu()
  while True:
    op = int(input("Qual operação você quer fazer? "))
    if op < 0 or op > len(funcs):
      print("Opção inválida!")
      continue

    if op == 0:
      break

    a = float(input("Digite o número: "))
    b = float(input("Digite o número: "))

    print(f"{a} {operacoes[op - 1]} {b} = {funcs[op - 1](a, b)}")
    menu()

main()
