quantasNotas = int(input("Quantas notas deseja: "))
somatorio = 0
for i in range(quantasNotas):
  nota = float(input("Digite a nota:"))
  somatorio += nota
media = somatorio/quantasNotas
print(media)