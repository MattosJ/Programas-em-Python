idade = int(input("Digite a idade: "))
somatorio = 0
qtd = 0
while idade > 0 :
  qtd += 1
  somatorio += idade
  idade = int(input("Digite a idade: "))


print(somatorio)
print(somatorio/qtd)