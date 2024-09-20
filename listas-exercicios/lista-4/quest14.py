numero = int(input("Digite o número: "))
if(numero == 0):
  numero = int(input("Digite o número: "))
somatorio = 0 
for i in range(1,numero+1):
  somatorio += 1/i

print(somatorio)