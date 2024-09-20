idade = int(input("Digite a idade: "))
tempoServico = float(input("Digite o tempo de serviço(em anos): "))
if((idade >= 65) and (tempoServico >= 30)):
  print("Pode se aposentar!")
else:
  print("Não pode se aposentar!")