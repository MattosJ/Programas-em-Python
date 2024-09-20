a = float(input("Digite um valor: "))
b = float(input("Digite um valor: "))
c = float(input("Digite um valor: "))
if(((a + b) > c) or ((a + c) > b) or ((b + c) > a)):
  if((a == b) and (b==c)) :
     print("Equilátero!")
  elif(((a==b) and (b != c)) or ((b==c) and (c != a)) or ((a == c) and (c != b))):
     print("Isósceles!")
  else:
     print("Escaleno!")