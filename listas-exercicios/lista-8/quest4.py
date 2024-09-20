nomeArquivo = input("Digite o nome do arquivo para ser aberto: ")
arq = open(nomeArquivo, "r")

conteudo = arq.read()
arq.close()

qtdCaracteres = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

alfabeto = "abcdefghijklmnopqrstuvwxyz"


for i in range(len(conteudo)):
  for j in range(26):
    if conteudo[i].lower() == alfabeto[j] :
      qtdCaracteres[j] += 1

print(qtdCaracteres)
