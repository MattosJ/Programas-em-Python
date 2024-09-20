arquivo = open("dados_resistencia.csv","r")
linhas = arquivo.readlines()

def Criarmatriz():
  matriz = []
  for linha in linhas:
    elementos = linha.strip().split(",")
    matriz.append(elementos)
  return matriz

matriz = Criarmatriz()
tamanhoMatriz = len(matriz)

def quantidade_tipo_de_material():
  aco = 0
  cimento = 0
  tijolo = 0
  concreto = 0
  madeira = 0
  for i in range(tamanhoMatriz):
    if(matriz[i][1] == "aco"):
      aco += 1
    elif(matriz[i][1] == "cimento"):
      cimento += 1
    elif(matriz[i][1] == "tijolo"):
      tijolo += 1
    elif(matriz[i][1] == "concreto"):
      concreto += 1
    elif(matriz[i][1] == "madeira"):
      madeira += 1

  return aco,cimento,tijolo,concreto,madeira

aco,cimento,tijolo,concreto,madeira = quantidade_tipo_de_material()

def menor_e_maior_carga_aplicada():
  maior =-9999999
  menor = 9999999
  for i in range(1,tamanhoMatriz):
    material = int(matriz[i][2])
    if material > maior:
      maior = material
    if material < menor:
      menor = material
  return maior,menor

maiorCarga,menorCarga = menor_e_maior_carga_aplicada()

def media_de_areas_da_secao_transversal_do_material_por_tipo():
  aco = 0
  somatorioaco= 0
  cimento = 0
  somatorioCimento = 0
  tijolo = 0
  somatorioTijolo = 0
  concreto = 0
  somatorioConcreto = 0
  madeira = 0
  somatorioMadeira = 0
  for i in range(1,tamanhoMatriz):
    material = matriz[i][1]
    area = int(matriz[i][3])
    if material == "aco":
      aco += 1
      somatorioaco += area
    elif material == "cimento":
      cimento += 1
      somatorioCimento += area
    elif material == "tijolo":
      tijolo += 1
      somatorioTijolo += area
    elif material == "concreto":
      concreto += 1
      somatorioConcreto += area
    elif material == "madeira":
      madeira += 1
      somatorioMadeira += area
  mediaAco = somatorioaco / aco
  mediaCimento  = somatorioCimento / cimento
  mediaTijolo = somatorioTijolo / tijolo
  mediaConcreto = somatorioConcreto / concreto
  mediaMadeira = somatorioMadeira / madeira
  return mediaAco,mediaCimento,mediaTijolo,mediaConcreto,mediaMadeira

mediaAco,mediaCimento,mediaTijolo,mediaConcreto,mediaMadeira = media_de_areas_da_secao_transversal_do_material_por_tipo()

def tensao_ruptura():
  
  maior =-9999999
  menor = 9999999
  materialMaior =""
  materialMenor =""
  for i in range(1,tamanhoMatriz):
    ruptura1 = int(matriz[i][4])
    ruptura2 = int(matriz[i][5])
    ruptura3 = int(matriz[i][6])
    material = matriz[i][1]
    media = (ruptura1 + ruptura2 + ruptura3) / 3
    if media > maior:
      maior = media
      materialMaior = material
    if media < menor:
      menor = media
      materialMenor = material
  return materialMaior, materialMenor

materialMaior,materialMenor = tensao_ruptura()

def gerarRelatorio():
  relatorio = open("relatorio_resistencia.txt","w")
  relatorio.write("Existem: " + str(aco) + " Acos" + "\n")
  relatorio.write("Existem: " + str(cimento)+ " Cimentos"+ "\n")
  relatorio.write("Existem: " + str(tijolo) + " Tijolos"+ "\n")
  relatorio.write("Existem: " + str(concreto) + " Concretos"+ "\n")
  relatorio.write("Existem: " + str(madeira) + " Madeiras"+ "\n")

gerarRelatorio()