n = int(input("Digite o número: "))
somatorio = 0
for i in range(1,n):
  if(n % i == 0):
    somatorio += i
print(somatorio)