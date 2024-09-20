a = int(input("Digite o número: "))
b = int(input("Digite o número: "))
divisivel = 0
if(a==b):
  print("Por favor digite um intervalo válido: ")
  a = int(input("Digite o número: "))
  b = int(input("Digite o número: "))
if(a > b):
  for i in range(b,a+1):
    if(i % 7 == 0):
      divisivel += 1
if(b > a):
  for i in range(a,b+1):
     if(i % 7 == 0):
      divisivel += 1
print(divisivel)