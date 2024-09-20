nota1 = float(input("Digite a nota: "))
nota2 = float(input("Digite a nota: "))
if(((nota1 < 0) or (nota1 > 10)) or (nota2 < 0) or (nota2 > 10)):
  print("Alguma nota é menor que 0 ou maior que 10!")
else:
  soma = nota1 + nota2
  media = soma / 2
  print(media)