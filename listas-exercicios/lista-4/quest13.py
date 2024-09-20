achou = False
i = 1
numero = int(input("Digite o número: "))
while not achou:
  if((((numero + i) % 7) == 0) and (((numero + i) % 11 )== 0) and (((numero + i) % 13) == 0)):
    achou = True
    print(numero+i)
  else:
    i+=1