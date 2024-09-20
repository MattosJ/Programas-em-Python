salario = float(input("Digite o salário: "))
emprestimo = float(input("Digite o valor da prestação do emprestimo desejado: "))

if((salario / 5) >= emprestimo ):
  print("Autorizado")
else:
  print("Negado")