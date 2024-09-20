caractere = input("Digite um caractere: ")
if( ord(caractere) >= 97 and (ord(caractere) <= 122)):
  print(caractere.upper())
else:
  print(caractere)