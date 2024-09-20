arq = open("agenda_telefonica.csv","a")
telefone = 1

while telefone != "0":
  contato = input("Digite o Nome: ")
  telefone = input("Digite o Telefone: ")
  if telefone != "0":
    arq.write(contato + ": " + telefone + "\n")
  
arq.close()