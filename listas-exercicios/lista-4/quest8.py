num = int(input("Digite o número: "))
if((num > 0) and (num < 3)):
  print("É primo!")
  exit()
else:
  for i in range(3,num):
    if(num % i == 0):
      print("Não é primo!")
      exit()
print("É primo!")
