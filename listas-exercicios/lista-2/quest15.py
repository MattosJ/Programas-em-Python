numero = int(input("Digite o número: "))
centena = numero//100
dezena = (numero//10) % 10
unidade = numero % 10

print(centena, dezena, unidade)