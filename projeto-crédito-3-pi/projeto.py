arquivo = open("dados_agricolas.csv","r")
linhas = arquivo.readlines()

def criandoMatriz():
   matriz = []
   for linha in linhas:
      elementos = linha.strip().split(",")
      matriz.append(elementos)
   return matriz

matriz = criandoMatriz()

def menu():
   print("Menu:")
   print("Para Criar o Relatório: (R)")
   print("Imprimir Relatório: (I), ATENÇÃO NECESSITA ANTES CRIAR O RELATÓRIO!")
   print("Sair: (S)")

def tela_inicial():
   opcao = " "
   while  opcao == " " :
      menu()
      opcao = input("Digite a opção desejada: ").upper()
      if(opcao =="R"):
         Relatorio()
      if(opcao == "I"):
         imprimirRelatorio()
      if(opcao == "S"):
         encerramento()
      else:
         opcao = " "

def quantidade():
   arroz =0
   soja = 0
   milho = 0
   feijao = 0
   cana = 0
   for i in range(len(matriz)):
      if(matriz[i][1] == "arroz"):
         arroz += 1
      elif(matriz[i][1] == "soja"):
         soja += 1
      elif(matriz[i][1] == "milho"):
         milho += 1
      elif(matriz[i][1] == "feijao"):
         feijao += 1
      elif(matriz[i][1] == "cana-de-acucar"):
       cana += 1
     
   return arroz,soja,milho,feijao,cana

Amostra_arroz,Amostra_soja,Amostra_milho,Amostra_feijao,Amostra_cana = quantidade()

def calcularArea():
   menorAreaPlantada = 9999999999999999999
   maiorAreaPlantada = -999999999999999999
   codigoMenor = 0
   codigoMaior = 0
   for i in range(1,len(matriz)):
      dado = int(matriz[i][2])
      if dado > maiorAreaPlantada:
         maiorAreaPlantada = int(matriz[i][2])
         codigoMaior = int(matriz[i][0])
      if dado < menorAreaPlantada:
         menorAreaPlantada = int(matriz[i][2])
         codigoMenor = int(matriz[i][0])

   return menorAreaPlantada,codigoMenor,maiorAreaPlantada,codigoMaior
   
resultado_Menor,resultado_codigoMenor,resultado_maior,resultado_codigoMaior = calcularArea()

def festilizantesOuPesticidas(soFetilizante = 0,soPesticidas = 0,ambos = 0,nehum = 0):
   for i in range(1,len(matriz)):
      dado1 = int(matriz[i][3])
      dado2 = int(matriz[i][4])
      if (dado1 != 0 ) and (dado2 == 0):
         soFetilizante += 1
      elif (dado2 != 0) and (dado1 == 0):
         soPesticidas += 1
      elif (dado1 != 0) and (dado2 != 0):
         ambos += 1
      else:
         nehum += 1

   return soFetilizante,soPesticidas,ambos,nehum
   
resultado_fetilizante,resultado_pesticidas,resultado_ambos,resultado_nenhum = festilizantesOuPesticidas()

def temperatura_Umidade_Precipitacao(maiorTemperatura = -999999999,maiorUmidade = -999999999,maiorPrecipitacao = -999999999):
   for i in range(1,len(matriz)):
      dado1 = int(matriz[i][5])
      dado2 = int(matriz[i][6])
      dado3 = int(matriz[i][7])
      if dado1 > maiorTemperatura:
         maiorTemperatura = dado1
      if dado2 > maiorUmidade:
         maiorUmidade = dado2
      if dado3 > maiorPrecipitacao:
         maiorPrecipitacao = dado3

   return maiorTemperatura, maiorUmidade, maiorPrecipitacao
resultado_temperatura,resultado_umidade,resultado_precipitacao = temperatura_Umidade_Precipitacao()


def Relatorio():
   relatorio = open("relatorio_cultivo.txt","w")
   relatorio.write("A maior Temperatura: " + str(resultado_temperatura) + "\n")
   relatorio.write("A maior Umidade: " + str(resultado_umidade) + "\n")
   relatorio.write("A maior precipitacao : " + str(resultado_precipitacao) + "\n")
   relatorio.write("Cultivos apenas com Fetilizantes: " + str(resultado_fetilizante) + "\n")
   relatorio.write("Cultivos apenas com Pesticidas: " + str(resultado_pesticidas) + "\n")
   relatorio.write("Cultivos  com Fetilizantes e Pesticidas: " + str(resultado_ambos) + "\n")
   relatorio.write("Cultivos sem  Fetilizantes e Sem Pesticidas: " + str(resultado_nenhum) + "\n")
   relatorio.write("A maior Area Plantada foi: " + str(resultado_maior)+" com codigo:" + str(resultado_codigoMaior) + "\n")
   relatorio.write("A menor Area Plantada foi: " + str(resultado_Menor)+" com codigo:" + str(resultado_codigoMenor) + "\n")
   relatorio.write("Existem "+ str(Amostra_arroz) + " Amostras de Arroz"+"\n")
   relatorio.write("Existem "+ str(Amostra_soja) + " Amostras de Soja"+"\n")
   relatorio.write("Existem "+ str(Amostra_milho) + " Amostras de Milho"+"\n")
   relatorio.write("Existem "+ str(Amostra_feijao) + " Amostras de Feijao"+"\n")
   relatorio.write("Existem "+ str(Amostra_cana) + " Amostras de Cana"+"\n")
   relatorio.close()


def imprimirRelatorio():
   relatorio = open("relatorio_cultivo.txt","r")
   linhas = relatorio.readlines()
   for i in range(len(linhas)):
      print(linhas[i])

def encerramento():
   print("Programa Encerrado!")
   exit()


tela_inicial()
